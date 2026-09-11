class BoundaryNodeClassifier:

    def __init__(self, model):

        self.model = model

    # =====================================================
    # Classify Boundary Nodes
    # =====================================================

    def classify(self):

        tol = 1e-6

        self.model.boundary_nodes = {

            "Left": [],

            "Right": [],

            "Bottom": [],

            "Top": [],

            "Hole": []

        }

        for node in self.model.nodes:

            x = node["x"]

            y = node["y"]

            # Left

            if abs(x) < tol:

                self.model.boundary_nodes["Left"].append(node["id"])

            # Right

            if abs(x - self.model.width) < tol:

                self.model.boundary_nodes["Right"].append(node["id"])

            # Bottom

            if abs(y) < tol:

                self.model.boundary_nodes["Bottom"].append(node["id"])

            # Top

            if abs(y - self.model.height) < tol:

                self.model.boundary_nodes["Top"].append(node["id"])

            # Hole

            if self.model.hole_radius > 0:

                dx = x - self.model.hole_x

                dy = y - self.model.hole_y

                if abs(

                    (dx * dx + dy * dy) ** 0.5

                    - self.model.hole_radius

                ) < tol:

                    self.model.boundary_nodes["Hole"].append(node["id"])

        print("\n========================")

        print("Boundary Nodes")

        print("========================")

        for key, value in self.model.boundary_nodes.items():

            print(

                f"{key:8s}: {len(value)}"

            )

        print("========================\n")