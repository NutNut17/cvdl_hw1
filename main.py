import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow

from src.controllers.display_controller import DisplayController
from src.controllers.load_controller import LoadController
from src.controllers.calibration_controller import CalibrationController
from src.controllers.ar_controller import ARController
from src.controllers.disparity_controller import DisparityController
from src.controllers.sift_controller import SiftController

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # Initialize controllers    
    DisplayController.initialize(window.display_widget)    
    
    load_controller = LoadController(window.load_image_widget, window.sift_widget)
    calibration_controller = CalibrationController(window.calibration_widget)
    ar_controller = ARController(window.ar_widget, calibration_controller)
    disparity_controller = DisparityController(window.disparity_widget)
    sift_controller = SiftController(window.sift_widget)
    
    # load_controller.load_folder("Dataset_CvDl_Hw1/Dataset_CvDl_Hw1/Q2_Image")
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()