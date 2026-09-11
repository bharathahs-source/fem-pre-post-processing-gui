class InputWriter:

    def __init__(self, model):

        self.model = model

    # =====================================================
    # Write Complete Input File
    # =====================================================

    def write(self, filename):

        with open(filename, "w") as f:

            self.write_header(f)

            self.write_elements(f)

            self.write_nodes(f)

            self.write_boundary_conditions(f)

            self.write_materials(f)

            self.write_loads(f)

    # =====================================================
    # Header
    # =====================================================

    def write_header(self, f):

        f.write("TITLE = FEM_GUI_V2\n\n")

        f.write("SPACE_DIMENSION = 2\n\n")

    # =====================================================
    # Elements
    # =====================================================

    def write_elements(self, f):

        ne = len(self.model.elements)

        # -------------------------------------------------
        # Number of Elements
        # -------------------------------------------------

        f.write(f"NUMBER_OF_ELEMENTS = {ne}\n\n")

        # -------------------------------------------------
        # Element Types
        # 1 = Triangle
        # 2 = Quadrilateral
        # -------------------------------------------------

        f.write("ELEMENT_TYPES =\n")

        count = 0

        for element in self.model.elements:

            if len(element["nodes"]) == 3:

                f.write("1 ")

            else:

                f.write("2 ")

            count += 1

            if count == 20:

                f.write("\n")

                count = 0

        f.write("\n\n")

        # -------------------------------------------------
        # INDEX_T
        # -------------------------------------------------

        f.write("INDEX_T =\n")

        start = 1

        for element in self.model.elements:

            end = start + len(element["nodes"]) - 1

            f.write(f"{start:8d}{end:8d}\n")

            start = end + 1

        f.write("\n")

        # -------------------------------------------------
        # T_VECTOR
        # -------------------------------------------------

        f.write("T_VECTOR =\n")

        count = 0

        for element in self.model.elements:

            for node in element["nodes"]:

                f.write(f"{node + 1:8d}")

                count += 1

                if count == 10:

                    f.write("\n")

                    count = 0

        if count != 0:

            f.write("\n")

        f.write("\n")

        # -------------------------------------------------
        # Material per Element
        # -------------------------------------------------

        f.write(

            f"MATERIAL_ELEMENT = {len(self.model.elements)}\n"

        )

        for element in self.model.elements:

            f.write(

                f"{element['material_id']}\n"

            )

        f.write("\n")

    # =====================================================
    # Nodes
    # =====================================================

    def write_nodes(self, f):

        nn = len(self.model.nodes)

        f.write(f"NODE_COORDINATES = {nn}\n")

        for node in self.model.nodes:

            f.write(

                f"{node['id'] + 1:8d} "

                f"{node['x']:18.8f} "

                f"{node['y']:18.8f}\n"

            )

        f.write("\n")
    # =====================================================
    # Boundary Conditions
    # =====================================================

    def write_boundary_conditions(self, f):

        prescribed = {}

        # ==============================================
        # Supports Only
        # ==============================================

        for bc in self.model.boundary_conditions:

            if bc["category"] != "Support":
                continue

            boundary = bc["boundary_name"]

            if boundary not in self.model.boundary_nodes:
                continue

            for node in self.model.boundary_nodes[boundary]:

                node_id = node + 1

                if node_id not in prescribed:

                    prescribed[node_id] = {

                        "fix_x": 0,
                        "fix_y": 0,
                        "ux": 0.0,
                        "uy": 0.0

                    }

                support = bc["support_type"]

                if support == "Fixed":

                    prescribed[node_id]["fix_x"] = 1
                    prescribed[node_id]["fix_y"] = 1

                elif support == "Roller X":

                    prescribed[node_id]["fix_x"] = 1

                elif support == "Roller Y":

                    prescribed[node_id]["fix_y"] = 1

                elif support == "Prescribed Displacement":

                    prescribed[node_id]["fix_x"] = 1
                    prescribed[node_id]["fix_y"] = 1

                    prescribed[node_id]["ux"] = bc["ux"]
                    prescribed[node_id]["uy"] = bc["uy"]

        f.write(

            f"NODES_WITH_PRESCRIBED_DISPLACEMENTS = {len(prescribed)}\n"

        )

        for node in sorted(prescribed.keys()):

            item = prescribed[node]

            f.write(

                f"{node:8d}"

                f"{item['fix_x']:4d}"

                f"{item['fix_y']:4d}"

                f"{item['ux']:20.12f}"

                f"{item['uy']:20.12f}\n"

            )

        f.write("\n")
    # =====================================================
    # Materials
    # =====================================================

    def write_materials(self, f):

        nm = len(self.model.materials)

        f.write(f"NUMBER_OF_MATERIALS = {nm}\n\n")

        f.write("MATERIAL_PROPERTIES =\n")

        for region in self.model.materials:

            f.write(

                f"{region['material_id']:6d}"

                f"{region['E']:18.8e}"

                f"{region['nu']:12.6f}"

                f"{region['rho']:15.4f}\n"

            )

        f.write("\n")
    # =====================================================
    # Write Loads
    # =====================================================

    def write_loads(self, f):

        print("\n==============================")
        print("Boundary Conditions")
        print("==============================")

        for bc in self.model.boundary_conditions:
            print(bc)

        print("\n==============================")
        print("Boundary Edges")
        print("==============================")

        if hasattr(self.model, "boundary_edges"):
            print(self.model.boundary_edges)
        else:
            print("boundary_edges DOES NOT EXIST")

        # ==============================================
        # Constant Body Force
        # ==============================================

        nm = len(self.model.materials)

        f.write(
            f"CONSTANT_BODY_FORCE = {nm}\n"
        )

        for material in self.model.materials:

            f.write(
                f"{material['material_id']:6d}"
                f"{0.0:20.12f}"
                f"{0.0:20.12f}\n"
            )

        f.write("\n")

        # ==============================================
        # Build Traction Records
        # ==============================================

        traction_records = []

        if not hasattr(self.model, "boundary_edges"):

            print("\nNo boundary_edges found.\n")

        else:

            for bc in self.model.boundary_conditions:

                if bc["category"] != "Load":
                    continue

                boundary = bc["boundary_name"]

                if boundary not in self.model.boundary_edges:
                    continue

                edges = self.model.boundary_edges[boundary]

                print(
                    f"\n{boundary} -> {len(edges)} boundary edges"
                )

                # -----------------------------------------
                # Force
                # -----------------------------------------

                if bc["load_type"] == "Force":

                    if bc["direction"] == "X":

                        fx = bc["value"]
                        fy = 0.0

                    else:

                        fx = 0.0
                        fy = bc["value"]

                # -----------------------------------------
                # Pressure
                # -----------------------------------------

                else:

                    if boundary == "Left":

                        fx = bc["value"]
                        fy = 0.0

                    elif boundary == "Right":

                        fx = -bc["value"]
                        fy = 0.0

                    elif boundary == "Top":

                        fx = 0.0
                        fy = -bc["value"]

                    elif boundary == "Bottom":

                        fx = 0.0
                        fy = bc["value"]

                    else:

                        fx = 0.0
                        fy = 0.0

                # -----------------------------------------
                # Create Traction Records
                # -----------------------------------------

                for edge in edges:

                    traction_records.append(

                        (

                            edge["element"],

                            edge["edge"],

                            fx,

                            fy

                        )

                    )

        # ==============================================
        # Write Section
        # ==============================================

        f.write(
            f"PRESCRIBED_TRACTIONS = {len(traction_records)}\n"
        )

        for element, local_edge, fx, fy in traction_records:

            f.write(
                f"{element:8d}"
                f"{local_edge:8d}"
                f"{fx:15.6f}"
                f"{fy:15.6f}\n"
            )

        
        f.write("\n")