class BoundaryEdgeClassifier:

    def __init__(self, model):

        self.model = model

    # =====================================================
    # Classify Boundary Edges
    # =====================================================

    def classify(self):

        tol = 1e-6

        self.model.boundary_edges = {

            "Left": [],
            "Right": [],
            "Bottom": [],
            "Top": [],
            "Hole": []

        }

        for element in self.model.elements:

            nodes = element["nodes"]

            # ------------------------------------------
            # Triangle
            # ------------------------------------------

            if len(nodes) == 3:

                edge_list = [

                    (nodes[0], nodes[1], 1),
                    (nodes[1], nodes[2], 2),
                    (nodes[2], nodes[0], 3)

                ]

            # ------------------------------------------
            # Quadrilateral
            # ------------------------------------------

            else:

                edge_list = [

                    (nodes[0], nodes[1], 1),
                    (nodes[1], nodes[2], 2),
                    (nodes[2], nodes[3], 3),
                    (nodes[3], nodes[0], 4)

                ]

            # ------------------------------------------
            # Check every edge
            # ------------------------------------------

            for n1, n2, local_edge in edge_list:

                p1 = self.model.nodes[n1]
                p2 = self.model.nodes[n2]

                x1 = p1["x"]
                y1 = p1["y"]

                x2 = p2["x"]
                y2 = p2["y"]

                # Left

                if abs(x1) < tol and abs(x2) < tol:

                    self.model.boundary_edges["Left"].append({

                        "element": element["id"],
                        "edge": local_edge

                    })

                # Right

                elif (

                    abs(x1 - self.model.width) < tol

                    and

                    abs(x2 - self.model.width) < tol

                ):

                    self.model.boundary_edges["Right"].append({

                        "element": element["id"],
                        "edge": local_edge

                    })

                # Bottom

                elif abs(y1) < tol and abs(y2) < tol:

                    self.model.boundary_edges["Bottom"].append({

                        "element": element["id"],
                        "edge": local_edge

                    })

                # Top

                elif (

                    abs(y1 - self.model.height) < tol

                    and

                    abs(y2 - self.model.height) < tol

                ):

                    self.model.boundary_edges["Top"].append({

                        "element": element["id"],
                        "edge": local_edge

                    })

                # Hole

                else:

                    r1 = (

                        (x1 - self.model.hole_x) ** 2 +

                        (y1 - self.model.hole_y) ** 2

                    ) ** 0.5

                    r2 = (

                        (x2 - self.model.hole_x) ** 2 +

                        (y2 - self.model.hole_y) ** 2

                    ) ** 0.5

                    if (

                        abs(r1 - self.model.hole_radius) < tol

                        and

                        abs(r2 - self.model.hole_radius) < tol

                    ):

                        self.model.boundary_edges["Hole"].append({

                            "element": element["id"],
                            "edge": local_edge

                        })