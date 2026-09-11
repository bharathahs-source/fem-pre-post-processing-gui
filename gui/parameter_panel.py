from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QGroupBox,
    QDockWidget,
    QPushButton,
    QScrollArea
)

from gui.geometry_preview import update_geometry_preview
from gui.boundary_manager import (add_boundary_condition, update_boundary_manager)


def create_parameter_panel(window):

    # ====================================================
    # Dock Widget
    # ====================================================

    dock = QDockWidget("Parameters", window)

    panel_scroll = QScrollArea()

    panel_scroll.setWidgetResizable(True)

    panel = QWidget()

    layout = QVBoxLayout(panel)

    # ====================================================
    # Geometry
    # ====================================================

    geometry = QGroupBox("Geometry")

    g_layout = QVBoxLayout()

    g_layout.addWidget(QLabel("Width"))
    window.width_input = QLineEdit("40")
    g_layout.addWidget(window.width_input)

    g_layout.addWidget(QLabel("Height"))
    window.height_input = QLineEdit("20")
    g_layout.addWidget(window.height_input)

    g_layout.addWidget(QLabel("X Interfaces"))
    window.x_interface_input = QLineEdit("20")
    g_layout.addWidget(window.x_interface_input)

    g_layout.addWidget(QLabel("Y Interfaces"))
    window.y_interface_input = QLineEdit("10")
    g_layout.addWidget(window.y_interface_input)

    g_layout.addWidget(QLabel("Hole Centre X"))
    window.hole_x_input = QLineEdit("20")
    g_layout.addWidget(window.hole_x_input)

    g_layout.addWidget(QLabel("Hole Centre Y"))
    window.hole_y_input = QLineEdit("10")
    g_layout.addWidget(window.hole_y_input)

    g_layout.addWidget(QLabel("Hole Radius"))
    window.hole_radius_input = QLineEdit("3")
    g_layout.addWidget(window.hole_radius_input)

    geometry.setLayout(g_layout)

    layout.addWidget(geometry)

    # ====================================================
    # Mesh
    # ====================================================

    mesh = QGroupBox("Mesh")

    mesh_layout = QVBoxLayout()

    mesh_layout.addWidget(QLabel("Mesh Size"))

    window.mesh_size_input = QLineEdit("0.5")

    mesh_layout.addWidget(window.mesh_size_input)

    mesh_layout.addWidget(QLabel("Element Type"))

    window.element_type_combo = QComboBox()

    window.element_type_combo.addItems([
        "Triangle",
        "Quadrilateral"
    ])

    mesh_layout.addWidget(window.element_type_combo)

    mesh.setLayout(mesh_layout)

    layout.addWidget(mesh)

    # ====================================================
    # Materials
    # ====================================================

    materials = QGroupBox("Materials")

    materials_layout = QVBoxLayout()

    window.material_count_label = QLabel(
        "Regions : 1"
    )

    materials_layout.addWidget(
        window.material_count_label
    )

    material_scroll = QScrollArea()

    material_scroll.setWidgetResizable(True)

    material_scroll.setMinimumHeight(220)

    window.material_widget = QWidget()

    window.material_layout = QVBoxLayout(
        window.material_widget
    )

    material_scroll.setWidget(
        window.material_widget
    )

    materials_layout.addWidget(
        material_scroll
    )

    materials.setLayout(materials_layout)

    layout.addWidget(materials)

    # ====================================================
    # Boundary Conditions
    # ====================================================

    bc = QGroupBox("Boundary Conditions")

    bc_layout = QVBoxLayout()

    # ---------------------------------------
    # Add Boundary Condition Button
    # ---------------------------------------

    window.add_bc_button = QPushButton(
        "+ Add Boundary Condition"
    )

    window.add_bc_button.clicked.connect(

        lambda: add_boundary_condition(window)

    )

    bc_layout.addWidget(
        window.add_bc_button
    )

    # ---------------------------------------
    # Boundary Cards Area
    # ---------------------------------------

    window.bc_widget = QWidget()

    window.bc_layout = QVBoxLayout(
        window.bc_widget
    )

    bc_scroll = QScrollArea()

    bc_scroll.setWidgetResizable(True)

    bc_scroll.setMinimumHeight(250)

    bc_scroll.setWidget(
        window.bc_widget
    )

    bc_layout.addWidget(
        bc_scroll
    )

    bc.setLayout(
        bc_layout
    )

    layout.addWidget(
        bc
    )
    
    # ====================================================
    # Mesh Information
    # ====================================================

    info = QGroupBox("Mesh Information")

    info_layout = QVBoxLayout()

    window.nodes_label = QLabel("Nodes : 0")
    window.elements_label = QLabel("Elements : 0")
    window.triangles_label = QLabel("Triangles : 0")
    window.quads_label = QLabel("Quadrilaterals : 0")
    window.dofs_label = QLabel("DOFs : 0")

    info_layout.addWidget(window.nodes_label)
    info_layout.addWidget(window.elements_label)
    info_layout.addWidget(window.triangles_label)
    info_layout.addWidget(window.quads_label)
    info_layout.addWidget(window.dofs_label)

    info.setLayout(info_layout)

    layout.addWidget(info)

    layout.addStretch()

    # ====================================================
    # Main Scroll Area
    # ====================================================

    panel_scroll.setWidget(panel)

    dock.setWidget(panel_scroll)

    window.addDockWidget(
        Qt.DockWidgetArea.LeftDockWidgetArea,
        dock
    )

    # ====================================================
    # Live Geometry Updates
    # ====================================================

    widgets = [

        window.width_input,
        window.height_input,
        window.x_interface_input,
        window.y_interface_input,
        window.hole_x_input,
        window.hole_y_input,
        window.hole_radius_input,
        window.mesh_size_input

    ]

    for widget in widgets:

        widget.editingFinished.connect(
            lambda: update_geometry_preview(window)
        )

    window.element_type_combo.currentIndexChanged.connect(
        lambda: update_geometry_preview(window)
    )

    update_geometry_preview(window)

    update_boundary_manager(window)

    