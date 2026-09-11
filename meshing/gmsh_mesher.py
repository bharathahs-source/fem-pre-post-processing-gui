import gmsh

from meshing.geometry_builder import GeometryBuilder
from meshing.mesh_reader import MeshReader
from meshing.mesh_classifier import MeshClassifier
from meshing.material_assigner import MaterialAssigner
from meshing.boundary_node_classifier import BoundaryNodeClassifier
from meshing.boundary_edge_classifier import BoundaryEdgeClassifier


class GmshMesher:

    def __init__(self, model):

        self.model = model

        self.geometry_builder = GeometryBuilder(model)

        self.mesh_reader = MeshReader(model)

        self.mesh_classifier = MeshClassifier(model)

        self.material_assigner = MaterialAssigner(model)

        self.boundary_node_classifier = BoundaryNodeClassifier(model)

        self.boundary_edge_classifier = BoundaryEdgeClassifier(model)

    # =====================================================
    # Generate Mesh
    # =====================================================

    def generate(self):

        gmsh.initialize()

        gmsh.model.add("FEM_Model")

        try:

            # ==============================================
            # Build CAD Geometry
            # ==============================================

            self.geometry_builder.build()

            # ==============================================
            # Generate Mesh
            # ==============================================

            gmsh.model.mesh.generate(2)

            # ==============================================
            # Read Mesh
            # ==============================================

            self.mesh_reader.read()

            # ==============================================
            # Boundary Classification
            # ==============================================

            self.boundary_node_classifier.classify()

            self.boundary_edge_classifier.classify()

            # ==============================================
            # Assign Materials
            # ==============================================

            self.material_assigner.assign()

            # ==============================================
            # Mesh Classification
            # ==============================================

            self.mesh_classifier.classify()

            # ==============================================
            # Print Summary
            # ==============================================

            self.mesh_reader.print_summary()

        finally:

            gmsh.finalize()