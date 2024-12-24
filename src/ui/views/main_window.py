from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("密码管理器")
        self.setGeometry(100, 100, 800, 600)  # 设置窗口位置和大小
        
        # 创建中心窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 添加一个测试按钮
        test_button = QPushButton("测试按钮")
        layout.addWidget(test_button) 