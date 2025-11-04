from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QTextEdit

class LoadImageWidget(QGroupBox):
    """Widget for loading images."""
    
    def __init__(self, parent=None):
        super().__init__("Load Image", parent)
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        
        self.btn_load_folder = QPushButton("Load Folder")
        self.btn_load_image_l = QPushButton("Load Image_L")
        self.btn_load_image_r = QPushButton("Load Image_R")
        
        layout.addWidget(self.btn_load_folder)
        layout.addWidget(self.btn_load_image_l)
        layout.addWidget(self.btn_load_image_r)               
        layout.addStretch()        
        self.setLayout(layout)
        
    def log_debug(self, message):
        """Add debug message to text area"""
        self.debug_text.append(message)