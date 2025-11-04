import cv2
import numpy as np
from typing import List

def chessboard_intrinsic(object_points: List[np.ndarray], corners_points: List[np.ndarray]):
    
    # Parameters
    image_size = (2048, 2048)    

    ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
        object_points, corners_points, image_size, None, None
    )

    return ret, camera_matrix, dist_coeffs, rvecs, tvecs
