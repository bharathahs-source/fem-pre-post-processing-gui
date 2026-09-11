from postprocessing.vtu_reader import VTUReader


if __name__ == "__main__":
    reader = VTUReader()
    reader.read("examples/input.vtu")
