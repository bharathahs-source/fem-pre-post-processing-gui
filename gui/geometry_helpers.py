from matplotlib.patches import Circle


# =====================================================
# Boundary Coordinates
# =====================================================

def get_boundary_coordinates(model, boundary_name):

    if boundary_name == "Left":

        return (
            0,
            0,
            0,
            model.height
        )

    elif boundary_name == "Right":

        return (
            model.width,
            0,
            model.width,
            model.height
        )

    elif boundary_name == "Bottom":

        return (
            0,
            0,
            model.width,
            0
        )

    elif boundary_name == "Top":

        return (
            0,
            model.height,
            model.width,
            model.height
        )

    return None


# =====================================================
# Hole Patch
# =====================================================

def get_hole_patch(model):

    return Circle(

        (
            model.hole_x,
            model.hole_y
        ),

        model.hole_radius,

        fill=False,

        edgecolor="royalblue",

        linewidth=3,

        zorder=250

    )