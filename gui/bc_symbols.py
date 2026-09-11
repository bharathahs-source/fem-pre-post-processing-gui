import numpy as np


# =====================================================
# Fixed Support
# =====================================================

def draw_fixed(ax, x1, y1, x2, y2):

    n = 12

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            ax.plot(
                [x1 - 0.45, x1],
                [y - 0.35, y],
                color="royalblue",
                linewidth=1.8,
                zorder=300
            )

            ax.plot(
                [x1 - 0.45, x1],
                [y + 0.35, y],
                color="royalblue",
                linewidth=1.8,
                zorder=300
            )

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            ax.plot(
                [x - 0.35, x],
                [y1 - 0.45, y1],
                color="royalblue",
                linewidth=1.8,
                zorder=300
            )

            ax.plot(
                [x + 0.35, x],
                [y1 - 0.45, y1],
                color="royalblue",
                linewidth=1.8,
                zorder=300
            )


# =====================================================
# Roller X
# =====================================================

def draw_roller_x(ax, x1, y1, x2, y2):

    n = 10

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            ax.plot(
                x1 - 0.4,
                y,
                marker="o",
                markersize=6,
                color="green",
                zorder=300
            )

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            ax.plot(
                x,
                y1 - 0.4,
                marker="o",
                markersize=6,
                color="green",
                zorder=300
            )


# =====================================================
# Roller Y
# =====================================================

def draw_roller_y(ax, x1, y1, x2, y2):

    n = 10

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            ax.plot(
                x1 + 0.4,
                y,
                marker="o",
                markersize=6,
                color="green",
                zorder=300
            )

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            ax.plot(
                x,
                y1 + 0.4,
                marker="o",
                markersize=6,
                color="green",
                zorder=300
            )


# =====================================================
# Prescribed Displacement
# =====================================================

def draw_prescribed(ax, x1, y1, x2, y2):

    n = 6

    if abs(x1 - x2) < 1e-6:

        ys = np.linspace(y1, y2, n)

        for y in ys:

            ax.arrow(

                x1 - 0.6,

                y,

                0.45,

                0,

                head_width=0.18,

                head_length=0.15,

                color="orange",

                length_includes_head=True,

                zorder=300

            )

    else:

        xs = np.linspace(x1, x2, n)

        for x in xs:

            ax.arrow(

                x,

                y1 - 0.6,

                0,

                0.45,

                head_width=0.18,

                head_length=0.15,

                color="orange",

                length_includes_head=True,

                zorder=300

            )