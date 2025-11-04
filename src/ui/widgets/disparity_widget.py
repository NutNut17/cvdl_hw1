from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton

class DisparityWidget(QGroupBox):
    """Widget for disparity map operations."""
    
    def __init__(self, parent=None):
        super().__init__("3. Disparity", parent)
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        
        self.btn_disparity = QPushButton("3.1 Disparity")
        
        layout.addWidget(self.btn_disparity)
        layout.addStretch()
        
        self.setLayout(layout)