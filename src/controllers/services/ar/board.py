import cv2
import numpy as np
from typing import List

def show_on_board(images: List[np.ndarray], text_aug: str, calibration_data_intrinsic):

    text_aug = text_aug[:6]
    fs = cv2.FileStorage('Dataset_CvDl_Hw1/Q2_Image/Q2_db/alphabet_db_onboard.txt', cv2.FILE_STORAGE_READ)

    ins = calibration_data_intrinsic["camera_matrix"]
    dist = calibration_data_intrinsic["dist_coeffs"]    
    rvecs = calibration_data_intrinsic["rvecs"]
    tvecs = calibration_data_intrinsic["tvecs"]
    
    positions_3D = np.array([
        [7, 5, 0], [4, 5, 0], [1, 5, 0],
        [7, 2, 0], [4, 2, 0], [1, 2, 0]
    ], dtype=np.float32)
    
    res_images = []
    
    for i in range(len(images)):
        image = images[i].copy()
        
        # Convert grayscale to BGR color space if needed
        if len(image.shape) == 2:  # Check if image is grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            
        rvec = rvecs[i]
        tvec = tvecs[i]
        
        for j, char in enumerate(text_aug):
            # 3. Get the 3D lines for this character
            # .mat() returns an array like (3, 2, 3) for 'K'
            char_lines_3D = fs.getNode(char).mat()
            if char_lines_3D is None:
                print(f"Character '{char}' not found in database.")
                continue
            
            # 4. Translate the letter to its correct 3D position
            # We add the j-th position vector to all points of the letter
            pos_vec = positions_3D[j]
            translated_lines_3D = char_lines_3D + pos_vec
            translated_lines_3D = translated_lines_3D * 0.02
            
            # 5. Reshape for cv2.projectPoints
            # projectPoints wants an (N, 3) array
            # Our array is (num_lines, 2, 3)
            # We reshape it to (num_lines * 2, 3)
            num_lines = translated_lines_3D.shape[0]
            points_to_project = translated_lines_3D.reshape(-1, 3)
            
            # 6. PROJECT! This is the magic.
            # It maps our 3D points to 2D pixel coordinates
            projected_points_2D, _ = cv2.projectPoints(
                points_to_project,
                rvec,
                tvec,
                ins,
                dist
            )
            
            # projected_points_2D is now (num_lines * 2, 1, 2)
            # Reshape to (num_lines, 2, 2) to easily get p1 and p2
            projected_lines_2D = projected_points_2D.reshape(num_lines, 2, 2)
            for line in projected_lines_2D:
                p1 = tuple(np.int32(line[0]))
                p2 = tuple(np.int32(line[1]))
                cv2.line(image, p1, p2, (0, 0, 255), 3) # Draw in red

        res_images.append(image)
    
    fs.release()
    
    return res_images 
