import numpy as np


# =====================================================
# Force
# =====================================================

def draw_force(ax, x1, y1, x2, y2, direction, magnitude):

    n = 6

    sign = 1 if magnitude >= 0 else -1

    # ==========================================
    # Vertical Boundary
    # ==========================================

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            if direction == "X":

                dx = 0.6 * sign

                ax.arrow(

                    x1,

                    y,

                    dx,

                    0,

                    color="crimson",

                    head_width=0.18,

                    head_length=0.15,

                    linewidth=2,

                    length_includes_head=True,

                    zorder=300

                )

            else:

                dy = 0.6 * sign

                ax.arrow(

                    x1,

                    y,

                    0,

                    dy,

                    color="crimson",

                    head_width=0.18,

                    head_length=0.15,

                    linewidth=2,

                    length_includes_head=True,

                    zorder=300

                )

    # ==========================================
    # Horizontal Boundary
    # ==========================================

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            if direction == "X":

                dx = 0.6 * sign

                ax.arrow(

                    x,

                    y1,

                    dx,

                    0,

                    color="crimson",

                    head_width=0.18,

                    head_length=0.15,

                    linewidth=2,

                    length_includes_head=True,

                    zorder=300

                )

            else:

                dy = 0.6 * sign

                ax.arrow(

                    x,

                    y1,

                    0,

                    dy,

                    color="crimson",

                    head_width=0.18,

                    head_length=0.15,

                    linewidth=2,

                    length_includes_head=True,

                    zorder=300

                )
# =====================================================
# Pressure
# =====================================================

def draw_pressure(ax, x1, y1, x2, y2, magnitude):

    n = 8

    sign = 1 if magnitude >= 0 else -1

    # ==========================================
    # Vertical Boundary
    # ==========================================

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            ax.arrow(

                x1 + 0.6 * sign,

                y,

                -0.45 * sign,

                0,

                color="darkred",

                head_width=0.15,

                head_length=0.15,

                linewidth=2,

                length_includes_head=True,

                zorder=300

            )

    # ==========================================
    # Horizontal Boundary
    # ==========================================

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            ax.arrow(

                x,

                y1 + 0.6 * sign,

                0,

                -0.45 * sign,

                color="darkred",

                head_width=0.15,

                head_length=0.15,

                linewidth=2,

                length_includes_head=True,

                zorder=300

            )