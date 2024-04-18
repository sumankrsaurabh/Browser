from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QPushButton, QSizePolicy, QScrollBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
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
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.browser.urlChanged.connect(self.update_AddressBar)
        self.setCentralWidget(self.browser)

        self.status_bar = self.statusBar()
        self.status_bar.setVisible(False)

        self.navigation_bar = QToolBar('Navigation Toolbar')
        self.navigation_bar.setMovable(False)  # Make the toolbar non-movable
        self.addToolBar(self.navigation_bar)

        back_button = QAction(QIcon("./assets/back_icon.png"), "Back", self)
        back_button.setStatusTip('Go to previous page you visited')
        back_button.triggered.connect(self.browser.back)
        self.navigation_bar.addAction(back_button)

        refresh_button = QAction(QIcon("./assets/refresh_icon.png"), "Refresh", self)
        refresh_button.setStatusTip('Refresh this page')
        refresh_button.triggered.connect(self.browser.reload)
        self.navigation_bar.addAction(refresh_button)

        next_button = QAction(QIcon("./assets/next_icon.png"), "Next", self)
        next_button.setStatusTip('Go to next page')
        next_button.triggered.connect(self.browser.forward)
        self.navigation_bar.addAction(next_button)

        home_button = QAction(QIcon("./assets/home_icon.png"), "Home", self)
        home_button.setStatusTip('Go to home page (Google page)')
        home_button.triggered.connect(self.go_to_home)
        self.navigation_bar.addAction(home_button)

        self.URLBar = QLineEdit()
        self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))
        self.navigation_bar.addWidget(self.URLBar)

        # Create a toggle button for the side panel
        self.toggle_button = QPushButton(QIcon("./assets/side_panel_icon.png"), "", self)
        self.toggle_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.toggle_button.setCheckable(True)
        self.toggle_button.clicked.connect(self.toggle_side_panel)

        # Add the toggle button to the toolbar
        self.navigation_bar.addWidget(self.toggle_button)

        # Apply the custom font to the main window and toolbar
        self.setFont(font)
        self.navigation_bar.setFont(font)

        # Apply scrollbar styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
            }
            QToolBar {
                background-color: #ffffff;
                border: none;
                spacing: 0px;
                padding-left: 16px;
                padding-right: 16px;
            }
            QLineEdit {
                background-color: transparent;
                border: 2px solid #ccc;
                border-radius: 18px;
                padding: 8px 16px;
                margin-top: 4px;
                margin-bottom: 4px;
                margin-right: 16px;
                margin-left: 8px;
                font-size: 14px;
            }
            QPushButton {
                border: none;
                border-radius: 24px;
            }
        """)

        self.show()

    def toggle_side_panel(self):
        # Placeholder for side panel toggle
        pass

    def go_to_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def go_to_URL(self, url: QUrl):
        if url.scheme() == '':
            url.setScheme('https://')
        self.browser.setUrl(url)
        self.update_AddressBar(url)

    def update_AddressBar(self, url):
        self.URLBar.setText(url.toString())
        self.URLBar.setCursorPosition(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
