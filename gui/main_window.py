from PyQt6.QtWidgets import (
    QMainWindow,
    QStatusBar
)

from models.fem_model import FEMModel

from gui.toolbar import create_toolbar
from gui.parameter_panel import create_parameter_panel
from gui.canvas import create_canvas


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        # =====================================================
        # FEM Model
        # =====================================================

        self.model = FEMModel()

        # =====================================================
        # Display Mode
        # =====================================================

        self.display_mode = "Geometry"

        # Available Modes
        #
        # "Geometry"
        # "Mesh"
        # "Results"

        # =====================================================
        # Window
        # =====================================================

        self.setWindowTitle("FEM GUI V2")

        self.resize(1400, 850)

        # =====================================================
        # GUI
        # =====================================================

        create_toolbar(self)

        create_canvas(self)

        create_parameter_panel(self)

        # =====================================================
        # Status Bar
        # =====================================================

        self.setStatusBar(QStatusBar())

        self.statusBar().showMessage("Ready")