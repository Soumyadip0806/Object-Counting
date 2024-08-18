import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QStatusBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vehicle Actuated Automatic Traffic Signalling System")
        self.setGeometry(0, 0, 800, 600)

        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet("background-color: #002366; color: white;")

        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.header = QLabel("Actuated Automatic Traffic Signalling System", self.centralwidget)
        font = QFont()
        font.setPointSize(14)
        self.header.setFont(font)
        self.header.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.header)

        self.horizontalLayout = QHBoxLayout()

        self.rtsp_input = QLineEdit(self.centralwidget)
        self.rtsp_input.setPlaceholderText("Enter RTSP Link")
        self.rtsp_input.setStyleSheet("""
            QLineEdit {
                background: rgba(255, 255, 255, 0);
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #45a049;
                background: rgba(255, 255, 255, 0.1);
            }
        """)
        self.horizontalLayout.addWidget(self.rtsp_input)

        self.process_button = QPushButton("Process", self.centralwidget)
        self.process_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.horizontalLayout.addWidget(self.process_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.video_label = QLabel(self.centralwidget)
        self.video_label.setSizePolicy(self.video_label.sizePolicy().Expanding, self.video_label.sizePolicy().Expanding)
        self.video_label.setStyleSheet("background-color: black;")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.video_label)

        self.count_label = QLabel("Object Counts: ", self.centralwidget)
        self.count_label.setMinimumSize(185, 50)
        font = QFont()
        font.setPointSize(16)
        self.count_label.setFont(font)
        self.count_label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.count_label, alignment=Qt.AlignLeft)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
