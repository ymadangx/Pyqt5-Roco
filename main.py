import sys
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QColorDialog, QMenu, QAction, QLabel
from PyQt5.QtCore import QUrl, QDateTime
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        datetime = QDateTime.currentDateTime()
        NowTime = datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.setWindowTitle("Gake辅助" + " " + "当前时间" + " " + NowTime)
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 创建一个WebEngineView来显示HTML页面
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # 创建一个按钮来刷新页面
        self.refresh_button = QPushButton("点击刷新当前游戏")
        self.refresh_button.clicked.connect(self.load_game)
        layout.addWidget(self.refresh_button)

        # 创建一个按钮来修改程序颜色
        self.color_button = QPushButton("修改该程序颜色")
        self.color_button.clicked.connect(self.change_color)
        layout.addWidget(self.color_button)

        # 创建一个按钮来执行JavaScript
        self.js_button = QPushButton("重新登录")
        self.js_button.clicked.connect(self.run_js)
        layout.addWidget(self.js_button)

        # 创建按钮来执行JavaScript操作
        self.modify_content_button = QPushButton("点击修改网站js")
        self.modify_content_button.clicked.connect(self.modify_content)
        layout.addWidget(self.modify_content_button)

        # 创建一个按钮来关闭程序
        self.close_button = QPushButton("关闭程序")
        self.close_button.clicked.connect(self.close_program)
        layout.addWidget(self.close_button)

        # 创建按钮来暂停和恢复网站线程
        self.pause_button = QPushButton("暂停网站线程")
        self.pause_button.clicked.connect(self.pause_threads)
        layout.addWidget(self.pause_button)

        self.resume_button = QPushButton("恢复网站线程")
        self.resume_button.clicked.connect(self.resume_threads)
        layout.addWidget(self.resume_button)

        # 加载游戏函数
        self.load_game()
        self.load_ui()

    def load_ui(self):
        icon = QIcon("gk_icon3.ico")
        self.setWindowIcon(icon)

    def run_js(self):
        js_code = "alert('请进行重新选区');"
        url = QUrl("https://17roco.qq.com/qzone.html")
        self.web_view.load(url)
        self.web_view.page().runJavaScript(js_code)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            # Apply the selected color to the main window and its child widgets
            r, g, b, a = color.red(), color.green(), color.blue(), color.alpha()
            stylesheet = f"background-color: rgba({r}, {g}, {b}, {a});"
            self.setStyleSheet(stylesheet)

    def load_game(self):
        url = QUrl("https://17roco.qq.com/qzone.html")
        self.web_view.load(url)

    def modify_content(self):
        js_code = """
        document.body.style.backgroundColor = 'lightblue';
        if (!document.getElementById('greeting')) {
            var greeting = document.createElement('div');
            greeting.id = 'greeting';
            greeting.innerHTML = '<h1>Gaoke辅助防伪码</h1>';
            document.body.appendChild(greeting);
        } else {
            document.getElementById('greeting').innerHTML = '<h1>Updated Hello from PyQt!</h1>';
        }
        """
        self.web_view.page().runJavaScript(js_code)

    def pause_threads(self):
        js_code = """
        window.originalSetTimeout = window.setTimeout;
        window.originalSetInterval = window.setInterval;
        window.setTimeout = function() {};
        window.setInterval = function() {};
        """
        self.web_view.page().runJavaScript(js_code)

    def resume_threads(self):
        js_code = """
        window.setTimeout = window.originalSetTimeout;
        window.setInterval = window.originalSetInterval;
        """
        self.web_view.page().runJavaScript(js_code)

    def close_program(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
