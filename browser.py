from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a toolbar and add navigation buttons
        self.toolbar = QtWidgets.QToolBar()
        self.addToolBar(self.toolbar)
        self.back_action = QtWidgets.QAction(QtGui.QIcon("backward.png"), "", self) #add your img here you can use and extension (.png,.jpg,etc)
        self.forward_action = QtWidgets.QAction(QtGui.QIcon("forward.png"), "", self) #add your img here you can use and extension (.png,.jpg,etc)
        self.refresh_action = QtWidgets.QAction(QtGui.QIcon("refresh.png"), "", self) #add your img here you can use and extension (.png,.jpg,etc)
        self.toolbar.addAction(self.back_action)
        self.toolbar.addAction(self.forward_action)
        self.toolbar.addAction(self.refresh_action)

        # Create a URL bar
        self.url_bar = QtWidgets.QLineEdit()
        self.toolbar.addWidget(self.url_bar)

        # Create a web view
        self.web_view = QtWebEngineWidgets.QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        # Connect the navigation buttons to the web view's methods
        self.back_action.triggered.connect(self.web_view.back)
        self.forward_action.triggered.connect(self.web_view.forward)
        self.refresh_action.triggered.connect(self.web_view.reload)

        # Connect the URL bar to the web view's load method
        self.url_bar.returnPressed.connect(self._load_url)

        # Connect the web view's urlChanged signal to the URL bar's setText slot
        self.web_view.urlChanged.connect(self._update_url_bar)

        # Set the window title and size
        self.setWindowTitle("My Web Browser")
        self.setGeometry(50, 50, 800, 600)

        # Load a default URL
        self.web_view.load(QtCore.QUrl("https://www.google.com"))
        self.show()

    def _load_url(self):
        """Load the URL entered in the URL bar"""
        url = self.url_bar.text()
        self.web_view.load(QtCore.QUrl(url))

    def _update_url_bar(self, url):
        """Update the URL bar with the current URL"""
        self.url_bar.setText(url.toString())
        self.url_bar.setCursorPosition(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    browser = Browser()
    app.exec_()
