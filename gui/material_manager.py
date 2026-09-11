from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QFrame,
    QSizePolicy
)


def update_material_value(region, key, widget):

    try:

        region[key] = float(widget.text())

    except ValueError:

        widget.setText(str(region[key]))


def update_material_manager(window):

    layout = window.material_layout

    # =====================================================
    # Clear Existing Widgets
    # =====================================================

    while layout.count():

        item = layout.takeAt(0)

        if item.widget():

            item.widget().deleteLater()

    # =====================================================
    # Region Count
    # =====================================================

    n_regions = len(window.model.materials)

    window.material_count_label.setText(
        f"Regions : {n_regions}"
    )

    # =====================================================
    # Create Material Cards
    # =====================================================

    for region in window.model.materials:

        card = QFrame()

        card.setFrameShape(QFrame.Shape.NoFrame)

        card.setSizePolicy(

            QSizePolicy.Policy.Expanding,

            QSizePolicy.Policy.Maximum

        )

        card.setStyleSheet("""

        QFrame{

            background:#F5F5F5;

            border:1px solid #D5D5D5;

            border-radius:10px;

        }

        QLabel{

            background:transparent;

            border:none;

        }

        QLineEdit{

            padding:6px;

            border:1px solid #BDBDBD;

            border-radius:6px;

            background:white;

        }

        """)

        card_layout = QVBoxLayout(card)

        card_layout.setContentsMargins(
            12,
            12,
            12,
            12
        )

        card_layout.setSpacing(8)

        # =====================================================
        # Title
        # =====================================================

        title = QLabel(
            f"Material Region {region['id']}"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet("""

            font-size:15px;

            font-weight:bold;

            color:#1F2937;

            border:none;

        """)

        card_layout.addWidget(title)

        # =====================================================
        # Young's Modulus
        # =====================================================

        card_layout.addWidget(
            QLabel("Young's Modulus (E)")
        )

        e_input = QLineEdit(
            f"{region['E']:.3e}"
        )

        e_input.editingFinished.connect(

            lambda r=region, w=e_input:

            update_material_value(r, "E", w)

        )

        card_layout.addWidget(e_input)

        # =====================================================
        # Poisson Ratio
        # =====================================================

        card_layout.addWidget(
            QLabel("Poisson Ratio (ν)")
        )

        nu_input = QLineEdit(
            str(region["nu"])
        )

        nu_input.editingFinished.connect(

            lambda r=region, w=nu_input:

            update_material_value(r, "nu", w)

        )

        card_layout.addWidget(nu_input)

        # =====================================================
        # Density
        # =====================================================

        card_layout.addWidget(
            QLabel("Density (ρ)")
        )

        rho_input = QLineEdit(
            str(region["rho"])
        )

        rho_input.editingFinished.connect(

            lambda r=region, w=rho_input:

            update_material_value(r, "rho", w)

        )

        card_layout.addWidget(rho_input)

        layout.addWidget(card)

    layout.addStretch()