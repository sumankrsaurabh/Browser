from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QGridLayout, QLabel, QPushButton, QComboBox, QFontDialog, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
import sys

class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        search_engine_label = QLabel("Search Engine:")
        layout.addWidget(search_engine_label)

        self.search_engine_combobox = QComboBox()
        self.search_engine_combobox.addItems(["Google", "Bing", "Yahoo"])
        layout.addWidget(self.search_engine_combobox)

        font_label = QLabel("Font:")
        layout.addWidget(font_label)

        self.font_button = QPushButton("Select Font")
        self.font_button.clicked.connect(self.open_font_dialog)
        layout.addWidget(self.font_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

    def open_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_button.setText(font.family())

    def save_settings(self):
        selected_search_engine = self.search_engine_combobox.currentText()
        selected_font = self.font_button.text()
        print("Selected Search Engine:", selected_search_engine)
        print("Selected Font:", selected_font)

class BrowserWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.browser_button = QPushButton("Open Browser", self)
        self.browser_button.clicked.connect(self.open_browser)
        layout.addWidget(self.browser_button)

    def open_browser(self):
        print("Open Browser")

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setWindowTitle("PythonGeeks Web Browser")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.browser_window = BrowserWindow(self)
        self.settings_window = SettingsWindow(self)

        self.stacked_widget.addWidget(self.browser_window)
        self.stacked_widget.addWidget(self.settings_window)

    def switch_to_browser(self):
        self.stacked_widget.setCurrentWidget(self.browser_window)

    def switch_to_settings(self):
        self.stacked_widget.setCurrentWidget(self.settings_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
