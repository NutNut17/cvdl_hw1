from .services.calibration.chessboard_corner import chessboard_corner
from .services.calibration.chessboard_intrinsic import chessboard_intrinsic
from .services.calibration.chessboard_extrinsic import chessboard_extrinsic
from .services.calibration.chessboard_undistort import chessboard_undistort
from .display_controller import DisplayController

class CalibrationController:
    
    def __init__(self, calibration_widget):
        self.widget = calibration_widget
        self.calibration_data_corners = {}
        self.calibration_object_points = {}
        self.calibration_data_intrinsic = {}
        self.calibration_data_extrinsic = {}
        self.calibration_data_rotation = {}
        self.calibration_data_distortion = {}
        self.images = []
        self._connect_signals()
        
    def _connect_signals(self):
        self.widget.btn_find_corners.clicked.connect(self.find_corners)
        self.widget.btn_find_intrinsic.clicked.connect(self.find_intrinsic)
        self.widget.btn_find_extrinsic.clicked.connect(self.find_extrinsic)
        self.widget.btn_find_distortion.clicked.connect(self.find_distortion)
        self.widget.btn_show_result.clicked.connect(self.show_result)
        
    def find_corners(self):
        images = DisplayController.get_global_images("Folder")
        if images is None:
            DisplayController.log_message("Error: No folder images loaded")
            return
    
        object_points, corners_list, images_with_corners, successful_images = chessboard_corner(images)

        # Store results
        self.calibration_data_corners = corners_list
        self.calibration_object_points = object_points
        self.images = successful_images
        
        DisplayController.set_images(images_with_corners)

        found_count = len(corners_list) if corners_list is not None else 0
        total = len(images)
        DisplayController.log_message(f"\nFound corners in {found_count}/{total} images")
        
    def find_intrinsic(self):
        
        if self.calibration_data_corners is None or len(self.calibration_data_corners) == 0:
            DisplayController.log_message("Error: No corners data available. Please run 'Find Corners' first.")
            return
    
        ret, camera_matrix, dist_coeffs, rvecs, tvecs = chessboard_intrinsic(self.calibration_object_points, self.calibration_data_corners)

        # Store results
        self.calibration_data_intrinsic = {
            "ret": ret,
            "camera_matrix": camera_matrix,
            "dist_coeffs": dist_coeffs,
            "rvecs": rvecs,
            "tvecs": tvecs
        }
        DisplayController.log_message(f"Intrinsic parameters:\n{camera_matrix}")
        
    def find_extrinsic(self):
        """Find extrinsic parameters for the selected image."""
        if not self.calibration_data_intrinsic:
            DisplayController.log_message("Error: No intrinsic data available. Please run 'Find Intrinsic' first.")
            return
        
        rotation_matrices, extrinsic_matrices = chessboard_extrinsic(self.calibration_data_intrinsic)
        
        # Create a dictionary mapping combo box indices (1-15) to matrices
        self.calibration_data_extrinsic = {
            str(i+1): matrix for i, matrix in enumerate(extrinsic_matrices)
        }
        self.calibration_data_rotation = {
            str(i+1): matrix for i, matrix in enumerate(rotation_matrices)
        }
        
        # Get currently selected index
        current_idx = self.widget.combo_extrinsic.currentText()
        if current_idx in self.calibration_data_extrinsic:
            extrinsic_matrix = self.calibration_data_extrinsic[current_idx]
            DisplayController.log_message(f"\nExtrinsic matrix for image {current_idx}:\n{extrinsic_matrix}")
        
    def find_distortion(self):
        if not self.calibration_data_intrinsic:
            DisplayController.log_message("Error: No intrinsic data available. Please run 'Find Intrinsic' first.")
            return
        DisplayController.log_message(f"\nDistortion coefficients:\n{self.calibration_data_intrinsic['dist_coeffs']}")
        
    def show_result(self):
        if not self.calibration_data_intrinsic:
            DisplayController.log_message("Error: No intrinsic data available. Please run 'Find Intrinsic' first.")
            return
        
        images = chessboard_undistort(self.images, self.calibration_data_intrinsic)
        DisplayController.set_images(images)