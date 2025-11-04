from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout

class CalibrationWidget(QGroupBox):
    """Widget for camera calibration operations."""
    
    def __init__(self, parent=None):
        super().__init__("1. Calibration", parent)
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        
        self.btn_find_corners = QPushButton("1.1 Find Corners")
        self.btn_find_intrinsic = QPushButton("1.2 Find Intrinsic")
        
        # Extrinsic sub-layout
        extrinsic_layout = QHBoxLayout()
        self.combo_extrinsic = QComboBox()
        self.combo_extrinsic.addItems([str(i) for i in range(1, 16)])
        self.btn_find_extrinsic = QPushButton("1.3 Find Extrinsic")
        extrinsic_layout.addWidget(self.combo_extrinsic)
        extrinsic_layout.addWidget(self.btn_find_extrinsic)
        
        self.btn_find_distortion = QPushButton("1.4 Find Distortion")
        self.btn_show_result = QPushButton("1.5 Show Result")
        
        layout.addWidget(self.btn_find_corners)
        layout.addWidget(self.btn_find_intrinsic)
        layout.addLayout(extrinsic_layout)
        layout.addWidget(self.btn_find_distortion)
        layout.addWidget(self.btn_show_result)
        layout.addStretch()
        
        self.setLayout(layout)