from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QComboBox,
    QLineEdit
)


# =====================================================
# Update Boundary
# =====================================================

def update_boundary(window, bc, value):

    boundary_ids = {

        "Left": 1,
        "Right": 2,
        "Bottom": 3,
        "Top": 4,
        "Hole": 5

    }

    bc["boundary_name"] = value
    bc["boundary_id"] = boundary_ids[value]

    window.renderer.draw(window.model)


# =====================================================
# Update Category
# =====================================================

def update_category(window, bc, value):

    bc["category"] = value

    update_boundary_manager(window)

    window.renderer.draw(window.model)


# =====================================================
# Update Support Type
# =====================================================

def update_support_type(window, bc, value):

    bc["support_type"] = value

    window.renderer.draw(window.model)


# =====================================================
# Update Load Type
# =====================================================

def update_load_type(window, bc, value):

    bc["load_type"] = value

    update_boundary_manager(window)

    window.renderer.draw(window.model)


# =====================================================
# Update Direction
# =====================================================

def update_direction(window, bc, value):

    bc["direction"] = value

    window.renderer.draw(window.model)


# =====================================================
# Update Magnitude
# =====================================================

def update_magnitude(bc, widget):

    try:

        bc["value"] = float(widget.text())

    except ValueError:

        widget.setText(str(bc["value"]))


# =====================================================
# Delete Boundary Condition
# =====================================================

def delete_boundary_condition(window, bc):

    window.model.boundary_conditions.remove(bc)

    update_boundary_manager(window)

    window.renderer.draw(window.model)


# =====================================================
# Add Boundary Condition
# =====================================================

def add_boundary_condition(window):

    bc = {

        "id": window.model.next_bc_id,

        "boundary_id": 1,

        "boundary_name": "Left",

        # -----------------------------------------
        # Category
        # -----------------------------------------

        "category": "Support",

        # -----------------------------------------
        # Support
        # -----------------------------------------

        "support_type": "Fixed",

        "ux": 0.0,

        "uy": 0.0,

        # -----------------------------------------
        # Load
        # -----------------------------------------

        "load_type": "Force",

        "direction": "X",

        "value": 1000.0

    }

    window.model.next_bc_id += 1

    window.model.boundary_conditions.append(bc)

    update_boundary_manager(window)

    window.renderer.draw(window.model)

# =====================================================
# Boundary Manager
# =====================================================

def update_boundary_manager(window):

    layout = window.bc_layout

    # ------------------------------------------
    # Clear Layout
    # ------------------------------------------

    while layout.count():

        item = layout.takeAt(0)

        if item.widget():

            item.widget().deleteLater()

    # ------------------------------------------
    # Create Cards
    # ------------------------------------------

    for bc in window.model.boundary_conditions:

        card = QFrame()

        card.setStyleSheet("""

        QFrame{

            background:#F5F5F5;

            border:1px solid #D5D5D5;

            border-radius:10px;

        }

        QLabel{

            border:none;

            background:transparent;

            font-weight:bold;

        }

        QLineEdit{

            padding:6px;

        }

        QComboBox{

            padding:4px;

        }

        QPushButton{

            background:#D9534F;

            color:white;

            padding:6px;

            border-radius:6px;

        }

        QPushButton:hover{

            background:#C9302C;

        }

        """)

        card_layout = QVBoxLayout(card)

        # ==========================================
        # Title
        # ==========================================

        title = QLabel(

            f"Boundary Condition {bc['id']}"

        )

        title.setAlignment(

            Qt.AlignmentFlag.AlignCenter

        )

        card_layout.addWidget(title)

        # ==========================================
        # Boundary
        # ==========================================

        card_layout.addWidget(

            QLabel("Boundary")

        )

        boundary_combo = QComboBox()

        boundary_combo.addItems([

            "Left",

            "Right",

            "Bottom",

            "Top",

            "Hole"

        ])

        boundary_combo.setCurrentText(

            bc["boundary_name"]

        )

        boundary_combo.currentTextChanged.connect(

            lambda value, b=bc:

            update_boundary(

                window,

                b,

                value

            )

        )

        card_layout.addWidget(boundary_combo)

        # ==========================================
        # Condition Category
        # ==========================================

        card_layout.addWidget(

            QLabel("Condition Type")

        )

        category_combo = QComboBox()

        category_combo.addItems([

            "Support",

            "Load"

        ])

        category_combo.setCurrentText(

            bc["category"]

        )

        category_combo.currentTextChanged.connect(

            lambda value, b=bc:

            update_category(

                window,

                b,

                value

            )

        )

        card_layout.addWidget(category_combo)
                # ==========================================
        # SUPPORT
        # ==========================================

        if bc["category"] == "Support":

            card_layout.addWidget(

                QLabel("Support Type")

            )

            support_combo = QComboBox()

            support_combo.addItems([

                "Fixed",

                "Roller X",

                "Roller Y",

                "Prescribed Displacement"

            ])

            support_combo.setCurrentText(

                bc["support_type"]

            )

            support_combo.currentTextChanged.connect(

                lambda value, b=bc:

                update_support_type(

                    window,

                    b,

                    value

                )

            )

            card_layout.addWidget(

                support_combo

            )

        # ==========================================
        # LOAD
        # ==========================================

        else:

            card_layout.addWidget(

                QLabel("Load Type")

            )

            load_combo = QComboBox()

            load_combo.addItems([

                "Force",

                "Pressure"

            ])

            load_combo.setCurrentText(

                bc["load_type"]

            )

            load_combo.currentTextChanged.connect(

                lambda value, b=bc:

                update_load_type(

                    window,

                    b,

                    value

                )

            )

            card_layout.addWidget(

                load_combo

            )

            # --------------------------------------
            # Force Direction
            # --------------------------------------

            if bc["load_type"] == "Force":

                card_layout.addWidget(

                    QLabel("Direction")

                )

                direction_combo = QComboBox()

                direction_combo.addItems([

                    "X",

                    "Y"

                ])

                direction_combo.setCurrentText(

                    bc["direction"]

                )

                direction_combo.currentTextChanged.connect(

                    lambda value, b=bc:

                    update_direction(

                        window,

                        b,

                        value

                    )

                )

                card_layout.addWidget(

                    direction_combo

                )

            # --------------------------------------
            # Magnitude
            # --------------------------------------

            card_layout.addWidget(

                QLabel("Magnitude")

            )

            magnitude = QLineEdit(

                str(bc["value"])

            )

            magnitude.editingFinished.connect(

                lambda b=bc, w=magnitude:

                update_magnitude(

                    b,

                    w

                )

            )

            card_layout.addWidget(

                magnitude

            )
                    # ==========================================
        # Delete Button
        # ==========================================

        delete_button = QPushButton(

            "Delete Boundary Condition"

        )

        delete_button.clicked.connect(

            lambda checked=False, b=bc:

            delete_boundary_condition(

                window,

                b

            )

        )

        card_layout.addWidget(

            delete_button

        )

        # ==========================================
        # Add Card to Layout
        # ==========================================

        layout.addWidget(

            card

        )

    # ==============================================
    # Stretch
    # ==============================================

    layout.addStretch()