from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
import cv2
from src.controllers.display_controller import DisplayController

class DisplayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()
    
    def _init_ui(self):
        
        layout = QHBoxLayout()
        
        # Left Image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # Right column: info label at top and Prev/Next at bottom
        self.right_layout = QVBoxLayout()
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setMaximumHeight(150)
        
        self.nav_layout = QHBoxLayout()        
        self.btn_prev = QPushButton("Previous")
        self.btn_next = QPushButton("Next")
        self.btn_next.clicked.connect(DisplayController.show_next_image)
        self.btn_prev.clicked.connect(DisplayController.show_prev_image)
        self.nav_layout.addWidget(self.btn_prev)
        self.nav_layout.addWidget(self.btn_next)
        self.nav_layout.addStretch()
        
        self.right_layout.addLayout(self.nav_layout)
        self.right_layout.addWidget(self.log_area)
        self.right_layout.addStretch()
        
        layout.addWidget(self.image_label, 7)
        layout.addLayout(self.right_layout, 3)
        self.setLayout(layout)

    def display_image(self, cv_img):
        if cv_img is None:
            return
        try:
            cv_img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        except Exception:
            cv_img_rgb = cv_img

        height, width = cv_img_rgb.shape[:2]
        bytes_per_line = 3 * width
        qt_img = QImage(cv_img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)

        # Scale pixmap to fit label while maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(self.image_label.size(),
                                        Qt.KeepAspectRatio,
                                        Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)

    def log_message(self, message):
        self.log_area.append(message)

    def clear_log(self):
        self.log_area.clear()