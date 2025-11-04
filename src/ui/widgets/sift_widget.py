from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton

class SIFTWidget(QGroupBox):
    """Widget for SIFT feature detection operations."""
    
    def __init__(self, parent=None):
        super().__init__("4. SIFT", parent)
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        
        self.btn_sift_load1 = QPushButton("Load Image 1")
        self.btn_sift_load2 = QPushButton("Load Image 2")
        self.btn_sift_keypoints = QPushButton("4.1 Keypoints")
        self.btn_sift_matched = QPushButton("4.2 Matched Keypoints")
        
        layout.addWidget(self.btn_sift_load1)
        layout.addWidget(self.btn_sift_load2)
        layout.addWidget(self.btn_sift_keypoints)
        layout.addWidget(self.btn_sift_matched)
        layout.addStretch()
        
        self.setLayout(layout)