from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QStatusBar, QLabel, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
import sys

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setWindowTitle("Personal Browser")
        self.setWindowIcon(QIcon("./assets/browser_icon.png"))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.browser.urlChanged.connect(self.update_AddressBar)
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

        self.addToolBarBreak()

        self.bookmarks_bar = QToolBar('Bookmarks Toolbar')
        self.addToolBar(self.bookmarks_bar)

        # Bookmarks
        self.add_bookmark("Facebook", "https://www.facebook.com", "./assets/facebook_icon.png")
        self.add_bookmark("LinkedIn", "https://www.linkedin.com", "./assets/linkedin_icon.png")
        
        self.show()

    def add_bookmark(self, name, url, icon_path):
        bookmark_button = QAction(QIcon(icon_path), name, self)
        bookmark_button.setStatusTip(f'Go to {name}')
        bookmark_button.triggered.connect(lambda: self.go_to_URL(QUrl(url)))
        self.bookmarks_bar.addAction(bookmark_button)

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
