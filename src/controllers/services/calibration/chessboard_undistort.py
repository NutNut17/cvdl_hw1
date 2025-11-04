import cv2
import numpy as np
from typing import List, Tuple

def chessboard_undistort(images: List[np.ndarray], calibration_data_intrinsic):

    ins = calibration_data_intrinsic["camera_matrix"]
    dist = calibration_data_intrinsic["dist_coeffs"]
    result_images = []

    for img in images:

        result_img = cv2.undistort(img, ins, dist)
        combined = np.hstack((img, result_img))
        result_images.append(combined)
            
    return result_images