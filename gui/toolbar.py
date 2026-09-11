from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import (
    QLabel,
    QComboBox
)

from gui.generate_mesh import generate_mesh
from gui.export_input import export_input

# =====================================================
# Update Colour Mode
# =====================================================

def update_color_mode(window, value):

    window.model.color_by = value

    window.renderer.draw(window.model)


# =====================================================
# Toolbar
# =====================================================

def create_toolbar(window):

    toolbar = window.addToolBar("Main")

    # ==========================================
    # New
    # ==========================================

    new_action = QAction("New", window)

    toolbar.addAction(new_action)

    # ==========================================
    # Generate Mesh
    # ==========================================

    mesh_action = QAction("Generate Mesh", window)

    mesh_action.triggered.connect(

        lambda: generate_mesh(window)

    )

    toolbar.addAction(mesh_action)

    # ==========================================
    # Colour By
    # ==========================================

    toolbar.addSeparator()

    toolbar.addWidget(QLabel("Color By : "))

    colour_combo = QComboBox()

    colour_combo.addItems([

        "Material ID",

        "Young's Modulus (E)",

        "Poisson Ratio (ν)",

        "Density (ρ)"

    ])

    colour_combo.currentTextChanged.connect(

        lambda value:

        update_color_mode(

            window,

            value

        )

    )

    toolbar.addWidget(colour_combo)

    # ==========================================
    # Export Input
    # ==========================================
    export_action = QAction(

        "Export Input",

        window 

    )

    export_action.triggered.connect(

        lambda: export_input(window)

    )

    toolbar.addAction(export_action)

    # Run Solver
    # ==========================================

    toolbar.addSeparator()

    solver_action = QAction("Run Solver", window)

    toolbar.addAction(solver_action)