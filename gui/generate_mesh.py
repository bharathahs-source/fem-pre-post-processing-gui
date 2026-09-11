from meshing.gmsh_mesher import GmshMesher

from gui.geometry_preview import update_geometry_preview


def generate_mesh(window):

    # =====================================================
    # Update Geometry
    # =====================================================

    update_geometry_preview(window)

    # =====================================================
    # Generate Mesh
    # =====================================================

    mesher = GmshMesher(window.model)

    mesher.generate()

    # =====================================================
    # Switch Renderer to Mesh Mode
    # =====================================================

    window.display_mode = "Mesh"

    window.renderer.draw(window.model)

    # =====================================================
    # Mesh Statistics
    # =====================================================

    n_nodes = len(window.model.nodes)

    n_elements = len(window.model.elements)

    n_triangles = n_elements

    n_quads = 0

    dofs = n_nodes * 2

    window.nodes_label.setText(
        f"Nodes : {n_nodes}"
    )

    window.elements_label.setText(
        f"Elements : {n_elements}"
    )

    window.triangles_label.setText(
        f"Triangles : {n_triangles}"
    )

    window.quads_label.setText(
        f"Quadrilaterals : {n_quads}"
    )

    window.dofs_label.setText(
        f"DOFs : {dofs}"
    )

    # =====================================================
    # Status
    # =====================================================

    window.statusBar().setStyleSheet(
        "color: green;"
    )

    window.statusBar().showMessage(
        "Mesh generated successfully."
    )