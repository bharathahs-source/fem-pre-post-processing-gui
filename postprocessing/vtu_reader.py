import pyvista as pv


class VTUReader:

    def __init__(self):

        self.mesh = None

    def read(self, filename):

        self.mesh = pv.read(filename)

        print("\n==========================")
        print("VTU FILE LOADED")
        print("==========================")

        print(self.mesh)

        print("\nPoint Data:")
        print(self.mesh.point_data)

        print("\nCell Data:")
        print(self.mesh.cell_data)

        print("\nAvailable Arrays:")
        print(self.mesh.array_names)

        print("\nNumber of Points:")
        print(self.mesh.n_points)

        print("Number of Cells:")
        print(self.mesh.n_cells)