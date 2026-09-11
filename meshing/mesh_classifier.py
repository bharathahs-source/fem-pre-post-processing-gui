from matplotlib.path import Path


class MeshClassifier:

    def __init__(self, model):

        self.model = model

    # =====================================================
    # Main Classification
    # =====================================================

    def classify(self):

        self.assign_materials()

        self.assign_boundaries()

    # =====================================================
    # Material Assignment
    # =====================================================

    def assign_materials(self):

        for element in self.model.elements:

            x, y = self.element_centroid(element)

            for region in self.model.materials:

                if (

                    region["xmin"] <= x <= region["xmax"]

                    and

                    region["ymin"] <= y <= region["ymax"]

                ):

                    element["material_id"] = region["material_id"]

                    break

    # =====================================================
    # Boundary Assignment
    # =====================================================

    def assign_boundaries(self):

        tolerance = 1e-6

        for bc in self.model.boundary_conditions:

            boundary_nodes = []

            for node in self.model.nodes:

                x = node["x"]

                y = node["y"]

                # ------------------------------------------
                # Left
                # ------------------------------------------

                if bc["boundary_name"] == "Left":

                    if abs(x) < tolerance:

                        boundary_nodes.append(node["id"])

                # ------------------------------------------
                # Right
                # ------------------------------------------

                elif bc["boundary_name"] == "Right":

                    if abs(x - self.model.width) < tolerance:

                        boundary_nodes.append(node["id"])

                # ------------------------------------------
                # Bottom
                # ------------------------------------------

                elif bc["boundary_name"] == "Bottom":

                    if abs(y) < tolerance:

                        boundary_nodes.append(node["id"])

                # ------------------------------------------
                # Top
                # ------------------------------------------

                elif bc["boundary_name"] == "Top":

                    if abs(y - self.model.height) < tolerance:

                        boundary_nodes.append(node["id"])

                # ------------------------------------------
                # Hole
                # ------------------------------------------

                elif bc["boundary_name"] == "Hole":

                    r = (

                        (x - self.model.hole_x) ** 2 +

                        (y - self.model.hole_y) ** 2

                    ) ** 0.5

                    if abs(r - self.model.hole_radius) < tolerance:

                        boundary_nodes.append(node["id"])

            bc["nodes"] = boundary_nodes

    # =====================================================
    # Element Centroid
    # =====================================================

    def element_centroid(self, element):

        pts = []

        for node_id in element["nodes"]:

            node = self.model.nodes[node_id]

            pts.append(

                (

                    node["x"],

                    node["y"]

                )

            )

        x = sum(p[0] for p in pts) / len(pts)

        y = sum(p[1] for p in pts) / len(pts)

        return x, y