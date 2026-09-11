def update_model(window):

    model = window.model

    model.width = float(window.width_input.text())

    model.height = float(window.height_input.text())

    model.hole_x = float(window.hole_x_input.text())

    model.hole_y = float(window.hole_y_input.text())

    model.hole_radius = float(window.hole_radius_input.text())

    model.mesh_size = float(window.mesh_size_input.text())

    model.element_type = window.element_type_combo.currentText()

    if window.x_interface_input.text().strip():

        model.x_interfaces = [

            float(v.strip())

            for v in window.x_interface_input.text().split(",")

            if v.strip()

        ]

    else:

        model.x_interfaces = []

    if window.y_interface_input.text().strip():

        model.y_interfaces = [

            float(v.strip())

            for v in window.y_interface_input.text().split(",")

            if v.strip()

        ]

    else:

        model.y_interfaces = []