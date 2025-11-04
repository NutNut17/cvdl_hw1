import cv2
import numpy as np
from .display_controller import DisplayController

class SiftController:
    
    def __init__(self, sift_widget):
        self.widget = sift_widget
        self._connect_signals()
        self.l_image = None
        self.r_image = None
        
        self.flag = None
        
        self.sift_kp1 = None
        self.sift_desc1 = None
        self.sift_gray1 = None
        
        self.sift_kp2 = None
        self.sift_desc2 = None
        self.sift_gray2 = None
        
    def _connect_signals(self):
        self.widget.btn_sift_load1.clicked.connect(self.load_image_l)
        self.widget.btn_sift_load2.clicked.connect(self.load_image_r)
        self.widget.btn_sift_keypoints.clicked.connect(self.sift_keypoints)
        self.widget.btn_sift_matched.clicked.connect(self.sift_matches)
        
    def load_image_l(self):
        self.flag = 'Left'
        
    def load_image_r(self):
        self.flag = 'Right'
        
    def sift_keypoints(self):        
        
        if not self.flag:
            DisplayController.log_message("Error: Please select Left or Right image to load first.")
            return
        
        if self.flag == 'Left':
            image = DisplayController.get_global_images("Left Image")
        else:
            image = DisplayController.get_global_images("Right Image")
        
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            DisplayController.log_message(f"Error: {self.flag} image not loaded.")
            return

        sift = cv2.SIFT_create()
        keypoints, descriptors = sift.detectAndCompute(gray, None)
        
        if self.flag == 'Left':
            self.sift_kp1 = keypoints
            self.sift_desc1 = descriptors
            self.sift_gray1 = gray # Save gray image for drawing matches later
        else:
            self.sift_kp2 = keypoints
            self.sift_desc2 = descriptors
            self.sift_gray2 = gray # Save gray image for drawing matches later
        
        print(f"Found {len(keypoints)} keypoints.")
        
        img_with_keypoints = cv2.drawKeypoints(
            gray, 
            keypoints, 
            None, # We're not passing an output image, so it creates one
            color=(0, 255, 0), # Color is (B,G,R), so this is green
            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
        )
        
        DisplayController.log_message(f"SIFT keypoints displayed for {self.flag} image.")   
        DisplayController.set_images([img_with_keypoints])
    
    def sift_matches(self):
        if self.sift_desc1 is None or self.sift_desc2 is None:
            DisplayController.log_message("Error: Please compute SIFT keypoints for both images first.")
            return
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(self.sift_desc1, self.sift_desc2, k=2)
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)
        print(f"Found {len(good_matches)} good matches.")
        DisplayController.log_message(f"Found {len(good_matches)} good matches.")
        img_matches = cv2.drawMatches(
            self.sift_gray1, 
            self.sift_kp1, 
            self.sift_gray2, 
            self.sift_kp2, 
            good_matches, 
            None, 
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )
        
        DisplayController.set_images([img_matches])
        DisplayController.log_message("SIFT matches displayed.")