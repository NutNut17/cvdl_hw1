import cv2
import numpy as np

def chessboard_extrinsic(calibration_data_intrinsic):
    """Calculate extrinsic parameters from calibration data.
    
    Args:
        calibration_data_intrinsic: Dictionary containing calibration data with rvecs and tvecs
        
    Returns:
        tuple: (rotation_matrices, extrinsic_matrices) for all calibration images
    """
    rvecs = calibration_data_intrinsic["rvecs"]
    tvecs = calibration_data_intrinsic["tvecs"]
    
    rotation_matrices = []
    extrinsic_matrices = []

    for rvec, tvec in zip(rvecs, tvecs):
        rotation_matrix, _ = cv2.Rodrigues(rvec)
        extrinsic_matrix = np.hstack((rotation_matrix, tvec))
        
        rotation_matrices.append(rotation_matrix)
        extrinsic_matrices.append(extrinsic_matrix)

    return rotation_matrices, extrinsic_matrices
