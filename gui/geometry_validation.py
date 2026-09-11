def validate_geometry(window):

    try:

        width = float(window.width_input.text())
        height = float(window.height_input.text())

        if width <= 0:
            return False, "❌ Width must be greater than zero."

        if height <= 0:
            return False, "❌ Height must be greater than zero."

        # ----------------------------
        # X Interfaces
        # ----------------------------

        if window.x_interface_input.text().strip():

            x_interfaces = [
                float(v.strip())
                for v in window.x_interface_input.text().split(",")
                if v.strip()
            ]

            for x in x_interfaces:

                if x <= 0 or x >= width:

                    return (
                        False,
                        f"❌ X Interface {x} must lie between 0 and {width}"
                    )

        # ----------------------------
        # Y Interfaces
        # ----------------------------

        if window.y_interface_input.text().strip():

            y_interfaces = [
                float(v.strip())
                for v in window.y_interface_input.text().split(",")
                if v.strip()
            ]

            for y in y_interfaces:

                if y <= 0 or y >= height:

                    return (
                        False,
                        f"❌ Y Interface {y} must lie between 0 and {height}"
                    )

        # ----------------------------
        # Hole
        # ----------------------------

        hole_x = float(window.hole_x_input.text())
        hole_y = float(window.hole_y_input.text())
        hole_r = float(window.hole_radius_input.text())

        if hole_r < 0:

            return False, "❌ Hole radius cannot be negative."

        if hole_r > 0:

            if hole_x - hole_r < 0:

                return False, "❌ Hole exceeds left boundary."

            if hole_x + hole_r > width:

                return False, "❌ Hole exceeds right boundary."

            if hole_y - hole_r < 0:

                return False, "❌ Hole exceeds bottom boundary."

            if hole_y + hole_r > height:

                return False, "❌ Hole exceeds top boundary."

        return True, "✅ Geometry Valid"

    except ValueError:

        return False, "❌ Please enter valid numeric values."