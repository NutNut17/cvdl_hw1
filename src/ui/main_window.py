from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from .widgets.load_image_widget import LoadImageWidget
from .widgets.display_widget import DisplayWidget
from .widgets.calibration_widget import CalibrationWidget
from .widgets.ar_widget import ARWidget
from .widgets.sift_widget import SIFTWidget
from .widgets.disparity_widget import DisparityWidget
from src.controllers.display_controller import DisplayController

class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homework 1 - Computer Vision and Deep Learning")
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the UI components."""
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        # Create widgets
        self.load_image_widget = LoadImageWidget()
        self.calibration_widget = CalibrationWidget()
        self.ar_widget = ARWidget()
        self.sift_widget = SIFTWidget()
        self.disparity_widget = DisparityWidget()
        self.display_widget = DisplayWidget()
        
        # Operation row (top)
        operation_layout = QHBoxLayout()
        
        # Column 3 (AR and SIFT)
        col_3_layout = QVBoxLayout()
        col_3_layout.addWidget(self.ar_widget)
        col_3_layout.addWidget(self.sift_widget)
        col_3_layout.addStretch()
        
        # Column 4 (Disparity)
        col_4_layout = QVBoxLayout()
        col_4_layout.addWidget(self.disparity_widget)
        col_4_layout.addStretch()
        
        # Add operation widgets to operation row
        operation_layout.addWidget(self.load_image_widget)
        operation_layout.addWidget(self.calibration_widget)
        operation_layout.addLayout(col_3_layout)
        operation_layout.addLayout(col_4_layout)
        
        # Debug and display row (bottom)
        display_layout = QHBoxLayout()
        display_layout.addWidget(self.display_widget)

        # Add both rows to main layout
        self.main_layout.addLayout(operation_layout)
        self.main_layout.addLayout(display_layout)

    # def set_controllers(self, display_controller, image_controller=None):
    #     """Wire controllers to UI elements. Call this after controllers are created.

    #     This connects the Prev/Next buttons to the display controller and stores
    #     references for future use.
    #     """
    #     self.display_controller = display_controller
    #     self.image_controller = image_controller

    #     # Connect nav buttons to display controller methods
    #     if hasattr(display_controller, 'show_prev_image'):
    #         self.btn_prev.clicked.connect(display_controller.show_prev_image)
    #     if hasattr(display_controller, 'show_next_image'):
    #         self.btn_next.clicked.connect(display_controller.show_next_image)

    # def set_info_text(self, text: str):
    #     self.info_label.setText(text)