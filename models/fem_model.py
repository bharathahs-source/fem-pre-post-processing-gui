from models.region_manager import RegionManager


class FEMModel:

    def __init__(self):

        # =====================================================
        # Geometry
        # =====================================================

        self.width = 40.0
        self.height = 20.0

        self.x_interfaces = []
        self.y_interfaces = []

        self.hole_x = 20.0
        self.hole_y = 10.0
        self.hole_radius = 3.0

        # =====================================================
        # Mesh
        # =====================================================

        self.mesh_size = 0.5

        self.element_type = "Triangle"

        self.nodes = []

        self.boundary_nodes = {
            "Left": [],
            "Right": [],
            "Bottom": [],
            "Top": [],
            "Hole": []
        }

        self.boundary_edges = {
            "Left": [],
            "Right": [],
            "Bottom": [],
            "Top": [],
            "Hole": []
        }
        self.elements = []

        # =====================================================
        # Materials / Regions
        # =====================================================

        self.materials = []

        self.region_manager = RegionManager(self)

        # =====================================================
        # Visualisation
        # =====================================================

        self.color_by = "Material ID"

        # =====================================================
        # Boundary Conditions
        # =====================================================

        self.boundary_conditions = []

        self.next_bc_id = 1

        
    # =====================================================
    # Region Generation
    # =====================================================

    def generate_regions(self):

        self.region_manager.generate_regions()