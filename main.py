# PyQt5 imports
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QStatusBar, QMenu, QVBoxLayout, QWidget, QPushButton, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon
# System import
import sys

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setWindowTitle("PythonGeeks Web Browser")
        self.setWindowIcon(QIcon("./assets/browser_icon.png"))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.browser.urlChanged.connect(self.update_AddressBar)
        self.browser.loadStarted.connect(self.loading_started)
        self.browser.loadFinished.connect(self.loading_finished)
        self.setCentralWidget(self.browser)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.navigation_bar = QToolBar('Navigation Toolbar')
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

        self.navigation_bar.addSeparator()

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

        # Create Bookmarks button
        self.bookmarks_button = QPushButton("Bookmarks")
        self.bookmarks_button.clicked.connect(self.show_bookmarks_panel)

        # Layout for side panel
        self.side_panel_layout = QVBoxLayout()
        self.side_panel_layout.addWidget(self.bookmarks_button)

        # Widget for side panel
        self.side_panel_widget = QWidget()
        self.side_panel_widget.setLayout(self.side_panel_layout)

        # Create a new toolbar for the side panel
        self.side_panel_toolbar = QToolBar('Side Panel')
        self.side_panel_toolbar.addWidget(self.side_panel_widget)

        # Add the side panel toolbar to the main window
        self.addToolBar(Qt.RightToolBarArea, self.side_panel_toolbar)

        # Initially hide the side panel
        self.side_panel_toolbar.setVisible(False)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            QToolBar {
                background-color: #f0f0f0;
                border: none;
                spacing: 10px;
            }
            QToolBar::item {
                padding: 0px;  /* Removed padding */
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 8px;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            QStatusBar {
                background-color: #e0e0e0;
                color: #333333;
            }
            QPushButton {
                border: none;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #dddddd; /* Change color on hover */
            }
        """)

        self.show()

    def show_bookmarks_panel(self):
        # Placeholder for bookmarks panel
        pass

    def toggle_side_panel(self):
        self.side_panel_toolbar.setVisible(not self.side_panel_toolbar.isVisible())

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

    def loading_started(self):
        self.status_bar.showMessage("Loading...")

    def loading_finished(self):
        self.status_bar.clearMessage()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
