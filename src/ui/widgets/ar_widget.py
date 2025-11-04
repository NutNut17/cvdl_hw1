from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QLineEdit

class ARWidget(QGroupBox):
    """Widget for Augmented Reality operations."""
    
    def __init__(self, parent=None):
        super().__init__("2. Augmented Reality", parent)
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        
        self.txt_aug = QLineEdit()
        self.btn_ar_board = QPushButton("2.1 Show Words on Board")
        self.btn_ar_vertical = QPushButton("2.2 Show Words Vertically")
        
        layout.addWidget(self.txt_aug)
        layout.addWidget(self.btn_ar_board)
        layout.addWidget(self.btn_ar_vertical)
        layout.addStretch()
        
        self.setLayout(layout)