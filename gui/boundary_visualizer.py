import numpy as np

from gui.geometry_helpers import (
    get_boundary_coordinates,
    get_hole_patch
)

from gui.load_symbols import (
    draw_force,
    draw_pressure
)


# =====================================================
# Draw Boundary Conditions
# =====================================================

def draw_boundary_conditions(ax, model):

    for bc in model.boundary_conditions:

        boundary = bc["boundary_name"]

        coords = get_boundary_coordinates(

            model,

            boundary

        )

        # -----------------------------------------
        # Hole
        # -----------------------------------------

        if boundary == "Hole":

            ax.add_patch(

                get_hole_patch(model)

            )

            continue

        if coords is None:

            continue

        x1, y1, x2, y2 = coords

        # =========================================
        # SUPPORTS
        # =========================================

        if bc["category"] == "Support":

            draw_support(

                ax,

                x1,

                y1,

                x2,

                y2,

                bc["support_type"]

            )

        # =========================================
        # LOADS
        # =========================================

        else:

            if bc["load_type"] == "Force":

                draw_force(

                    ax,

                    x1,

                    y1,

                    x2,

                    y2,

                    bc["direction"],

                    bc["value"]

                )

            else:

                draw_pressure(

                    ax,

                    x1,

                    y1,

                    x2,

                    y2,

                    bc["value"]

                )
                # =====================================================
# Draw Supports
# =====================================================

def draw_support(ax, x1, y1, x2, y2, support_type):

    n = 6

    # ==========================================
    # Vertical Boundary
    # ==========================================

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            # ----------------------------------
            # Fixed
            # ----------------------------------

            if support_type == "Fixed":

                ax.plot(

                    [x1 - 0.35, x1],
                    [y, y],

                    color="royalblue",

                    linewidth=2,

                    zorder=250

                )

            # ----------------------------------
            # Roller X
            # ----------------------------------

            elif support_type == "Roller X":

                ax.scatter(

                    x1 - 0.20,

                    y,

                    s=18,

                    color="royalblue",

                    zorder=250

                )

            # ----------------------------------
            # Roller Y
            # ----------------------------------

            elif support_type == "Roller Y":

                ax.plot(

                    [x1 - 0.25, x1],

                    [y, y],

                    "--",

                    color="royalblue",

                    linewidth=2,

                    zorder=250

                )

            # ----------------------------------
            # Prescribed Displacement
            # ----------------------------------

            elif support_type == "Prescribed Displacement":

                ax.arrow(

                    x1 - 0.6,

                    y,

                    0.45,

                    0,

                    color="green",

                    head_width=0.12,

                    head_length=0.12,

                    linewidth=2,

                    length_includes_head=True,

                    zorder=260

                )

    # ==========================================
    # Horizontal Boundary
    # ==========================================

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            # ----------------------------------
            # Fixed
            # ----------------------------------

            if support_type == "Fixed":

                ax.plot(

                    [x, x],

                    [y1 - 0.35, y1],

                    color="royalblue",

                    linewidth=2,

                    zorder=250

                )

            # ----------------------------------
            # Roller X
            # ----------------------------------

            elif support_type == "Roller X":

                ax.plot(

                    [x, x],

                    [y1 - 0.30, y1],

                    "--",

                    color="royalblue",

                    linewidth=2,

                    zorder=250

                )

            # ----------------------------------
            # Roller Y
            # ----------------------------------

            elif support_type == "Roller Y":

                ax.scatter(

                    x,

                    y1 - 0.20,

                    s=18,

                    color="royalblue",

                    zorder=250

                )

            # ----------------------------------
            # Prescribed Displacement
            # ----------------------------------

            elif support_type == "Prescribed Displacement":

                ax.arrow(

                    x,

                    y1 - 0.6,

                    0,

                    0.45,

                    color="green",

                    head_width=0.12,

                    head_length=0.12,

                    linewidth=2,

                    length_includes_head=True,

                    zorder=260

                )