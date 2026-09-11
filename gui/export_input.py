from PyQt6.QtWidgets import QFileDialog

from input_output.input_writer import InputWriter


def export_input(window):

    filename, _ = QFileDialog.getSaveFileName(

        window,

        "Export Input File",

        "input.txt",

        "Text Files (*.txt)"

    )

    if not filename:

        return

    writer = InputWriter(

        window.model

    )

    writer.write(

        filename

    )

    window.statusBar().showMessage(

        "Input file exported."

    )