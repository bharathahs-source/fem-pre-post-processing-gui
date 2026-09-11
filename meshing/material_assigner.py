class MaterialAssigner:

    def __init__(self, model):

        self.model = model

    # =====================================================
    # Point Inside Hole
    # =====================================================

    def inside_hole(self, x, y):

        if self.model.hole_radius <= 0:

            return False

        dx = x - self.model.hole_x

        dy = y - self.model.hole_y

        return dx * dx + dy * dy <= self.model.hole_radius ** 2

    # =====================================================
    # Assign Materials
    # =====================================================

    def assign(self):

        for element in self.model.elements:

            # ---------------------------------------------
            # Element centroid
            # ---------------------------------------------

            xc = 0.0
            yc = 0.0

            for node_id in element["nodes"]:

                node = self.model.nodes[node_id]

                xc += node["x"]
                yc += node["y"]

            xc /= len(element["nodes"])
            yc /= len(element["nodes"])

            # ---------------------------------------------
            # Ignore elements inside hole
            # ---------------------------------------------

            if self.inside_hole(xc, yc):

                element["material_id"] = -1

                continue

            # ---------------------------------------------
            # Find containing region
            # ---------------------------------------------

            assigned = False

            for region in self.model.materials:

                if (

                    region["xmin"] <= xc <= region["xmax"]

                    and

                    region["ymin"] <= yc <= region["ymax"]

                ):

                    element["material_id"] = region["material_id"]

                    assigned = True

                    break

            if not assigned:

                element["material_id"] = 1

        # =====================================================
        # Summary
        # =====================================================

        print("\n==============================")

        print("Material Assignment")

        print("==============================")

        for element in self.model.elements[:10]:

            print(

                f"Element {element['id']:4d} -> Material {element['material_id']}"

            )

        print("==============================\n")