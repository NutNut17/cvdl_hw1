import cv2
import numpy as np
from .display_controller import DisplayController

class DisparityController:
    
    def __init__(self, disparity_widget):
        self.widget = disparity_widget
        self._connect_signals()
        
    def _connect_signals(self):
        self.widget.btn_disparity.clicked.connect(self.disparity)
        
    def disparity(self):

        l_image = DisplayController.get_global_images("Left Image")
        r_image = DisplayController.get_global_images("Right Image")
        
        grayL = cv2.cvtColor(l_image, cv2.COLOR_BGR2GRAY)
        grayR = cv2.cvtColor(r_image, cv2.COLOR_BGR2GRAY)
        
        if l_image is None or r_image is None:
            DisplayController.log_message("Error: Left or Right image not loaded")
            return
        
        stereo = cv2.StereoBM.create(numDisparities=432, blockSize=25)
        disparity_image = stereo.compute(grayL, grayR)
        disparity_norm = cv2.normalize(disparity_image, None, alpha=0, beta=255,
                                     norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        # resized = cv2.resize(disparity_norm, (800, 600), interpolation=cv2.INTER_AREA)
        # cv2.imshow('diaparity', resized)

        DisplayController.set_images([disparity_norm])
        DisplayController.log_message("Displayed words on board.")
        
        