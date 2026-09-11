from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from gui.renderer import Renderer


def create_canvas(window):

    # =====================================================
    # Create Matplotlib Figure
    # =====================================================

    figure = Figure()

    canvas = FigureCanvasQTAgg(figure)

    window.figure = figure

    window.canvas = canvas

    # =====================================================
    # Renderer
    # =====================================================

    window.renderer = Renderer(window, canvas)

    # =====================================================
    # Central Widget
    # =====================================================

    window.setCentralWidget(canvas)