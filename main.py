from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QToolBar,
    QAction,
    QLineEdit,
    QPushButton,
    QSizePolicy,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl,QSize
from PyQt5.QtGui import QIcon, QFont
import sys


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # Load the custom font
        font = QFont()
        font.setFamily("Inter")  # Replace "YourCustomFont" with the actual font name

        self.setWindowTitle("Safest Browser")
        self.setWindowIcon(QIcon("./assets/browser_icon.png"))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.browser.urlChanged.connect(self.update_AddressBar)
        self.setCentralWidget(self.browser)

        self.status_bar = self.statusBar()
        self.status_bar.setVisible(False)

        self.navigation_bar = QToolBar("Navigation Toolbar")
        self.navigation_bar.setMovable(False)  # Make the toolbar non-movable
        self.addToolBar(self.navigation_bar)

        # Load png icons
        back_icon = QIcon("./assets/back_icon.png")
        refresh_icon = QIcon("./assets/refresh_icon.png")
        next_icon = QIcon("./assets/next_icon.png")
        home_icon = QIcon("./assets/home_icon.png")
        side_panel_icon = QIcon("./assets/menu_icon.png")

        # Create actions with png icons and set icon size
        button_size = QSize(24, 24)

        back_button = QAction(back_icon, "Back", self)
        back_icon_actual = back_icon.actualSize(button_size)
        back_button.setIcon(QIcon(back_icon.pixmap(back_icon_actual)))

        refresh_button = QAction(refresh_icon, "Refresh", self)
        refresh_icon_actual = refresh_icon.actualSize(button_size)
        refresh_button.setIcon(QIcon(refresh_icon.pixmap(refresh_icon_actual)))

        next_button = QAction(next_icon, "Next", self)
        next_icon_actual = next_icon.actualSize(button_size)
        next_button.setIcon(QIcon(next_icon.pixmap(next_icon_actual)))

        home_button = QAction(home_icon, "Home", self)
        home_icon_actual = home_icon.actualSize(button_size)
        home_button.setIcon(QIcon(home_icon.pixmap(home_icon_actual)))

        # Add actions to the toolbar
        self.navigation_bar.addAction(back_button)
        self.navigation_bar.addAction(refresh_button)
        self.navigation_bar.addAction(next_button)
        self.navigation_bar.addAction(home_button)

        self.URLBar = QLineEdit()
        self.URLBar.returnPressed.connect(self.on_URLBar_returnPressed)
        self.navigation_bar.addWidget(self.URLBar)

        # Create a toggle button for the side panel
        self.toggle_button = QPushButton(side_panel_icon, "", self)
        self.toggle_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setIconSize(button_size)
        self.toggle_button.clicked.connect(self.toggle_side_panel)

        # Add the toggle button to the toolbar
        self.navigation_bar.addWidget(self.toggle_button)

        # Apply the custom font to the main window and toolbar
        self.setFont(font)
        self.navigation_bar.setFont(font)

        # Apply scrollbar styling
        self.setStyleSheet(
            """
            QToolBar {
                background-color: #ffffff;
                border: none;
                spacing: 4px;
                border-bottom: 0.5px solid #ccc;
                padding: 2px;
            }
            QLineEdit {
                background-color: transparent;
                border: 1px solid #000000;
                border-radius: 14px;
                padding: 4px 16px;
                margin-top: 4px;
                margin-bottom: 4px;
                margin-right: 16px;
                margin-left: 8px;
                font-size: 14px;
            }
            QPushButton {
                border: none;
                padding: 8px 16px 8px 0px;
            }
        """
        )

        self.show()

    def toggle_side_panel(self):
        # Placeholder for side panel toggle
        pass

    def go_to_home(self):
        self.browser.setUrl(QUrl("https://www.google.com/"))

    def go_to_URL(self, url: QUrl):
        if url.scheme() == "":
            url.setScheme("https")
        self.browser.setUrl(url)
        self.update_AddressBar(url)

    def update_AddressBar(self, url):
        self.URLBar.setText(url.toString())
        self.URLBar.setCursorPosition(0)

    def on_URLBar_returnPressed(self):
        input_text = self.URLBar.text()
        if "." in input_text and " " not in input_text:
            url = QUrl(input_text)
            if url.isValid():
                self.go_to_URL(url)
            else:
                self.search_with_search_engine(input_text)
        else:
            self.search_with_search_engine(input_text)

    def search_with_search_engine(self, term):
        search_url = QUrl("https://www.google.com/search?q={}".format(term))
        self.browser.setUrl(search_url)
        self.update_AddressBar(search_url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
