class RegionManager:

    def __init__(self, model):

        self.model = model

        # =====================================================
        # Default Material Colours
        # =====================================================

        self.default_colors = [

            "#4F81BD",  # Blue
            "#C0504D",  # Red
            "#9BBB59",  # Green
            "#8064A2",  # Purple
            "#F79646",  # Orange
            "#4BACC6",  # Cyan
            "#948A54",  # Olive
            "#7F7F7F",  # Grey
            "#DA9694",  # Pink
            "#92CDDC"   # Light Blue

        ]

    # =====================================================
    # Generate Material Regions
    # =====================================================

    def generate_regions(self):

        # =====================================================
        # Preserve Existing Material Properties
        # =====================================================

        previous = {}

        for region in self.model.materials:

            previous[region["id"]] = {

                "E": region["E"],

                "nu": region["nu"],

                "rho": region["rho"],

                "color": region["color"]

            }

        # =====================================================
        # Build Regions
        # =====================================================

        regions = []

        x_lines = [0] + self.model.x_interfaces + [self.model.width]

        y_lines = [0] + self.model.y_interfaces + [self.model.height]

        region_id = 1

        for i in range(len(x_lines) - 1):

            xmin = x_lines[i]
            xmax = x_lines[i + 1]

            for j in range(len(y_lines) - 1):

                ymin = y_lines[j]
                ymax = y_lines[j + 1]

                # ==============================================
                # Preserve Existing Material
                # ==============================================

                if region_id in previous:

                    E = previous[region_id]["E"]

                    nu = previous[region_id]["nu"]

                    rho = previous[region_id]["rho"]

                    color = previous[region_id]["color"]

                else:

                    E = 210e9

                    nu = 0.30

                    rho = 7850

                    color = self.default_colors[
                        (region_id - 1)
                        % len(self.default_colors)
                    ]

                # ==============================================
                # Create Region
                # ==============================================

                regions.append({

                    "id": region_id,

                    "xmin": xmin,
                    "xmax": xmax,

                    "ymin": ymin,
                    "ymax": ymax,

                    "material_id": region_id,

                    "E": E,

                    "nu": nu,

                    "rho": rho,

                    "color": color

                })

                region_id += 1

        self.model.materials = regions

        return regions