import cv2
import numpy as np
from typing import List

def chessboard_corner(images: List[np.ndarray]):
    """Find chessboard corners in a list of images.

    Args:
        images: List of BGR images (numpy arrays).S

    Returns:
        corners_list: list of refined corner arrays for images where corners were found.
        images_with_corners: list of images (copied) with drawn corners; original image is included when corners are not found.
    """

    corners_list = []           # 2D corner points
    object_points = []          # 3D object points
    images_with_corners = []    # Images with drawn corners
    successful_images = []      # Images where corners were found

    # Parameters
    pattern_size = (11, 8)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    winSize = (5, 5)
    zeroZone = (-1, -1)
    
    chessboard_width = pattern_size[0]
    chessboard_height = pattern_size[1]

    objp = np.zeros((chessboard_width * chessboard_height, 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard_width, 0:chessboard_height].T.reshape(-1, 2)    
    objp = objp * 0.02 # Apply the 0.02m scale

    for idx, img in enumerate(images):
        if img is None:
            images_with_corners.append(None)
            continue
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)
        except Exception as e:
            print(f"\nError finding chessboard corners in image {idx+1}: {e}")
            images_with_corners.append(img)
            continue

        if ret and corners is not None:
            # 3D points
            object_points.append(objp)
            
            # 2D points (corners)
            corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
            corners_list.append(corners2)

            # Draw and display the corners
            img_corners = img.copy()
            cv2.drawChessboardCorners(img_corners, pattern_size, corners2, ret)
            images_with_corners.append(img_corners)
            successful_images.append(gray)

            print(f"\nFound corners in image {idx+1}")
        else:
            print(f"\nFailed to find corners in image {idx+1}")
            images_with_corners.append(img)

    return object_points, corners_list, images_with_corners, successful_images
