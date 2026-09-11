from gui.model_sync import update_model
from gui.geometry_validation import validate_geometry
from gui.material_manager import update_material_manager


def update_geometry_preview(window):

    # =====================================================
    # Update FEM Model
    # =====================================================

    update_model(window)

    # =====================================================
    # Validate Geometry
    # =====================================================

    valid, message = validate_geometry(window)

    if valid:

        window.statusBar().setStyleSheet(
            "color: green;"
        )

    else:

        window.statusBar().setStyleSheet(
            "color: red;"
        )

    window.statusBar().showMessage(message)

    if not valid:
        return

    # =====================================================
    # Generate Material Regions
    # =====================================================

    window.model.generate_regions()

    # =====================================================
    # Update Material Panel
    # =====================================================

    update_material_manager(window)

    # =====================================================
    # Draw Geometry
    # =====================================================

    window.renderer.draw(
        window.model
    )   