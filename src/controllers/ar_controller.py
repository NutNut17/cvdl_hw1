from .services.ar.board import show_on_board
from .services.ar.vertical import show_on_vertical
from .display_controller import DisplayController

class ARController:
    
    def __init__(self, ar_widget, calibration_controller):
        self.widget = ar_widget
        self.calibration_controller = calibration_controller
        self._connect_signals()
                
    def _connect_signals(self):
        self.widget.btn_ar_board.clicked.connect(self.show_board)
        self.widget.btn_ar_vertical.clicked.connect(self.show_vertical)      
        
    def show_board(self):
        
        if not self.calibration_controller.calibration_data_intrinsic:
            DisplayController.log_message("Error: Calibration data not available. Please run calibration first.")
            return
        
        processed_images = show_on_board(self.calibration_controller.images, self.widget.txt_aug.text().upper(), self.calibration_controller.calibration_data_intrinsic)
        DisplayController.set_images(processed_images)
        DisplayController.log_message("Displayed words on board.")
        
    def show_vertical(self):
        
        if not self.calibration_controller.calibration_data_intrinsic:
            DisplayController.log_message("Error: Calibration data not available. Please run calibration first.")
            return
        
        processed_images = show_on_vertical(self.calibration_controller.images, self.widget.txt_aug.text().upper(), self.calibration_controller.calibration_data_intrinsic)
        DisplayController.set_images(processed_images)
        DisplayController.log_message("Displayed vertical words on board.")