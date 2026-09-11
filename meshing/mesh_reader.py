import gmsh


class MeshReader:

    def __init__(self, model):

        self.model = model

        self.node_map = {}

    # =====================================================
    # Read Mesh
    # =====================================================

    def read(self):

        self.read_nodes()

        self.read_elements()

    # =====================================================
    # Read Nodes
    # =====================================================

    def read_nodes(self):

        self.model.nodes = []

        node_tags, coords, _ = gmsh.model.mesh.getNodes()

        self.node_map = {}

        for i, tag in enumerate(node_tags):

            x = coords[3 * i]

            y = coords[3 * i + 1]

            node = {

                "id": len(self.model.nodes),

                "tag": tag,

                "x": x,

                "y": y

            }

            self.node_map[tag] = node["id"]

            self.model.nodes.append(node)

    # =====================================================
    # Read Elements
    # =====================================================

    def read_elements(self):

        self.model.elements = []

        element_types, _, connectivities = gmsh.model.mesh.getElements()

        element_id = 1

        for element_type, connectivity in zip(

            element_types,

            connectivities

        ):

            # ---------------------------------------------
            # 2 = Linear Triangle
            # ---------------------------------------------

            if element_type != 2:

                continue

            for i in range(0, len(connectivity), 3):

                nodes = [

                    self.node_map[connectivity[i]],

                    self.node_map[connectivity[i + 1]],

                    self.node_map[connectivity[i + 2]]

                ]

                self.model.elements.append({

                    "id": element_id,

                    "nodes": nodes,

                    "material_id": None,

                    "boundary_ids": [],

                    "load_ids": []

                })

                element_id += 1

    # =====================================================
    # Mesh Summary
    # =====================================================

    def print_summary(self):

        print("\n==============================")

        print("Mesh Summary")

        print("==============================")

        print(f"Nodes     : {len(self.model.nodes)}")

        print(f"Elements  : {len(self.model.elements)}")

        print("==============================\n")