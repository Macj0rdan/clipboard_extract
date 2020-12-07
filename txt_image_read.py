from PIL import ImageGrab
import sys
from PyQt5 import QtWidgets, uic
import pytesseract
import config_ini


class GUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('main.ui', self)  # loads GUI file for GUI creation

        self.select_dir_btn = self.findChild(QtWidgets.QPushButton, "select_dir_btn")
        self.dir_text = self.findChild(QtWidgets.QLineEdit, "selected_dir_Qline_edit")
        self.select_dir_btn.pressed.connect(self.open_file)

        self.extract_button = self.findChild(QtWidgets.QPushButton, "extract_button")
        self.extract_button.pressed.connect(self.display_results)

        self.result_text = self.findChild(QtWidgets.QTextEdit, "result_text")

        self.path_tesseract = config_ini.config_rw().read_ini().get("Settings", "path")  # loads tesseract path from config file
        pytesseract.pytesseract.tesseract_cmd = self.path_tesseract
        self.dir_text.setText(self.path_tesseract)

        self.show()

    def open_file(self):
        self.txt_file = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", "C:\\")
        if not self.txt_file == "":
            self.dir_text.setText(self.txt_file)

    def display_results(self):
        self.result_text.setText(self.get_text_from_clipboard())

    def get_text_from_clipboard(self):
        image_from_clipboard = ImageGrab.grabclipboard()
        try:
            self.result_text.setStyleSheet("color: black;")
            return pytesseract.image_to_string(image_from_clipboard)
        except TypeError as e:
            if type(image_from_clipboard) == list:
                # Todo: Add way of reading files when more then one is copied
                return pytesseract.image_to_string(image_from_clipboard[0])
            else:
                self.result_text.setStyleSheet("color: red;")
                return "Exception while trying to read the image:\n    {}".format(e)
        except Exception as e:
            self.result_text.setStyleSheet("color: red;")
            return "Exception while trying to read the image:\n    {}".format(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    app.exec_()
