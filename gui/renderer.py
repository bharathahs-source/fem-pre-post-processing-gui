from matplotlib.patches import Circle
from matplotlib.patches import Rectangle

from gui.boundary_visualizer import draw_boundary_conditions
import matplotlib.cm as cm
import matplotlib.colors as mcolors

class Renderer:

    def __init__(self, window, canvas):

        self.window = window
        self.canvas = canvas

    # =====================================================
    # Region Colour
    # =====================================================

    def get_region_colour(self, model, region):

        mode = model.color_by

        # -------------------------------------------------
        # Material ID (categorical)
        # -------------------------------------------------

        if mode == "Material ID":

            colours = [

                "#4F81BD",
                "#C0504D",
                "#9BBB59",
                "#8064A2",
                "#F79646",
                "#4BACC6",
                "#948A54",
                "#7F7F7F",
                "#DA9694",
                "#92CDDC"

            ]

            return colours[
                (region["material_id"] - 1)
                % len(colours)
            ]

        # -------------------------------------------------
        # Continuous properties
        # -------------------------------------------------

        if mode == "Young's Modulus (E)":

            values = [r["E"] for r in model.materials]
            value = region["E"]

        elif mode == "Poisson Ratio (ν)":

            values = [r["nu"] for r in model.materials]
            value = region["nu"]

        elif mode == "Density (ρ)":

            values = [r["rho"] for r in model.materials]
            value = region["rho"]

        else:

            return "#DDDDDD"

        vmin = min(values)
        vmax = max(values)

        if abs(vmax - vmin) < 1e-12:

            return "#6FA8DC"

        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

        cmap = cm.get_cmap("turbo")

        return cmap(norm(value))

    # =====================================================
    # Main Draw Function
    # =====================================================

    def draw(self, model):
        print(f"Display Mode = {self.window.display_mode}")
        self.canvas.figure.clear()

        ax = self.canvas.figure.add_subplot(111)

        if self.window.display_mode == "Mesh":

            self.draw_mesh(ax, model)

        else:

            self.draw_geometry(ax, model)

        self.finish_plot(ax, model)

    # =====================================================
    # Draw Material Regions
    # =====================================================

    def draw_material_regions(self, ax, model):

        for region in model.materials:

            colour = self.get_region_colour(

                model,

                region

            )

            rect = Rectangle(

                (

                    region["xmin"],

                    region["ymin"]

                ),

                region["xmax"] - region["xmin"],

                region["ymax"] - region["ymin"],

                facecolor=colour,

                edgecolor="none",

                alpha=0.45,

                zorder=1

            )

            ax.add_patch(rect)

            xc = (

                region["xmin"] +

                region["xmax"]

            ) / 2

            yc = (

                region["ymin"] +

                region["ymax"]

            ) / 2

            ax.text(

                xc,

                yc,

                f"M{region['material_id']}",

                ha="center",

                va="center",

                fontsize=10,

                fontweight="bold",

                zorder=5

            )

    # =====================================================
    # Geometry View
    # =====================================================

    def draw_geometry(self, ax, model):

        # =====================================================
        # Draw Material Regions
        # =====================================================

        self.draw_material_regions(

            ax,

            model

        )

        # =====================================================
        # Draw Domain
        # =====================================================

        ax.plot(

            [0, model.width, model.width, 0, 0],

            [0, 0, model.height, model.height, 0],

            color="black",

            linewidth=2,

            zorder=20

        )

        # =====================================================
        # Draw X Interfaces
        # =====================================================

        for x in model.x_interfaces:

            ax.plot(

                [x, x],

                [0, model.height],

                "--",

                color="red",

                linewidth=1,

                zorder=21

            )

        # =====================================================
        # Draw Y Interfaces
        # =====================================================

        for y in model.y_interfaces:

            ax.plot(

                [0, model.width],

                [y, y],

                "--",

                color="orange",

                linewidth=1,

                zorder=21

            )

        # =====================================================
        # Draw Hole
        # =====================================================

        if model.hole_radius > 0:

            hole = Circle(

                (

                    model.hole_x,

                    model.hole_y

                ),

                model.hole_radius,

                facecolor="white",

                edgecolor="black",

                linewidth=2,

                zorder=30

            )

            ax.add_patch(hole)

        # =====================================================
        # Draw Boundary Conditions
        # =====================================================

        draw_boundary_conditions(

            ax,

            model

        )

        
    # =====================================================
    # Mesh View
    # =====================================================

    def draw_mesh(self, ax, model):

        # =====================================================
        # Draw Material Regions
        # =====================================================

        self.draw_material_regions(

            ax,

            model

        )

        # =====================================================
        # Draw Mesh
        # =====================================================

        for element in model.elements:

            pts = []

            for node_id in element["nodes"]:

                node = model.nodes[node_id]

                pts.append(

                    (

                        node["x"],

                        node["y"]

                    )

                )

            xs = [p[0] for p in pts]

            ys = [p[1] for p in pts]

            xs.append(xs[0])

            ys.append(ys[0])

            ax.plot(

                xs,

                ys,

                color="#8A8A8A",

                linewidth=0.35,

                zorder=10

            )

        # =====================================================
        # Draw Domain
        # =====================================================

        ax.plot(

            [0, model.width, model.width, 0, 0],

            [0, 0, model.height, model.height, 0],

            color="black",

            linewidth=2,

            zorder=20

        )

        # =====================================================
        # Draw Interfaces
        # =====================================================

        for x in model.x_interfaces:

            ax.plot(

                [x, x],

                [0, model.height],

                "--",

                color="red",

                linewidth=1,

                zorder=21

            )

        for y in model.y_interfaces:

            ax.plot(

                [0, model.width],

                [y, y],

                "--",

                color="orange",

                linewidth=1,

                zorder=21

            )

        # =====================================================
        # Draw Hole
        # =====================================================

        if model.hole_radius > 0:

            hole = Circle(

                (

                    model.hole_x,

                    model.hole_y

                ),

                model.hole_radius,

                facecolor="white",

                edgecolor="black",

                linewidth=2,

                zorder=30

            )

            ax.add_patch(hole)

        # =====================================================
        # Draw Boundary Conditions
        # =====================================================

        draw_boundary_conditions(

            ax,

            model

        )

    # =====================================================
    # Plot Formatting
    # =====================================================

    def finish_plot(self, ax, model):

        ax.set_title(

            f"Domain {model.width} × {model.height}"

        )

        ax.set_xlabel("X")

        ax.set_ylabel("Y")

        ax.set_xlim(-1, model.width + 1)

        ax.set_ylim(-1, model.height + 1)

        ax.set_aspect("equal")

        ax.grid(True)

        # =====================================================
        # Colour Bar
        # =====================================================

        if model.color_by != "Material ID":

            if model.color_by == "Young's Modulus (E)":

                values = [r["E"] for r in model.materials]

            elif model.color_by == "Poisson Ratio (ν)":

                values = [r["nu"] for r in model.materials]

            elif model.color_by == "Density (ρ)":

                values = [r["rho"] for r in model.materials]

            else:

                values = []

            if values:

                norm = mcolors.Normalize(

                    vmin=min(values),

                    vmax=max(values)

                )

                sm = cm.ScalarMappable(

                    norm=norm,

                    cmap="turbo"

                )

                sm.set_array([])

                self.canvas.figure.colorbar(

                    sm,

                    ax=ax,

                    shrink=0.85,

                    label=model.color_by

                )

        self.canvas.draw()