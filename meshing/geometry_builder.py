import gmsh


class GeometryBuilder:

    def __init__(self, model):

        self.model = model

        self.domain = None

        self.interface_curves = []

    # =====================================================
    # Build Geometry
    # =====================================================

    def build(self):

        self.create_domain()

        self.create_interfaces()

        self.fragment_geometry()

        self.create_hole()

        gmsh.model.occ.synchronize()

        self.apply_mesh_size()

    # =====================================================
    # Rectangle
    # =====================================================

    def create_domain(self):

        self.domain = gmsh.model.occ.addRectangle(

            0,
            0,
            0,

            self.model.width,

            self.model.height

        )

    # =====================================================
    # Create Interface Lines
    # =====================================================

    def create_interfaces(self):

        self.interface_curves.clear()

        # ---------------------------------------------
        # Vertical Interfaces
        # ---------------------------------------------

        for x in self.model.x_interfaces:

            line = gmsh.model.occ.addLine(

                gmsh.model.occ.addPoint(
                    x,
                    0,
                    0
                ),

                gmsh.model.occ.addPoint(
                    x,
                    self.model.height,
                    0
                )

            )

            self.interface_curves.append(
                (1, line)
            )

        # ---------------------------------------------
        # Horizontal Interfaces
        # ---------------------------------------------

        for y in self.model.y_interfaces:

            line = gmsh.model.occ.addLine(

                gmsh.model.occ.addPoint(
                    0,
                    y,
                    0
                ),

                gmsh.model.occ.addPoint(
                    self.model.width,
                    y,
                    0
                )

            )

            self.interface_curves.append(
                (1, line)
            )

    # =====================================================
    # Fragment Geometry
    # =====================================================

    def fragment_geometry(self):

        if not self.interface_curves:

            return

        gmsh.model.occ.fragment(

            [(2, self.domain)],

            self.interface_curves

        )

    # =====================================================
    # Create Hole
    # =====================================================

    def create_hole(self):

        if self.model.hole_radius <= 0:

            return

        hole = gmsh.model.occ.addDisk(

            self.model.hole_x,

            self.model.hole_y,

            0,

            self.model.hole_radius,

            self.model.hole_radius

        )

        surfaces = gmsh.model.occ.getEntities(2)

        gmsh.model.occ.cut(

            surfaces,

            [(2, hole)],

            removeObject=True,

            removeTool=True

        )

    # =====================================================
    # Mesh Size
    # =====================================================

    def apply_mesh_size(self):

        gmsh.option.setNumber(

            "Mesh.MeshSizeMin",

            self.model.mesh_size

        )

        gmsh.option.setNumber(

            "Mesh.MeshSizeMax",

            self.model.mesh_size

        )