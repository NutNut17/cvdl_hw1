from PyQt5.QtWidgets import QFileDialog
import cv2
import os
from datetime import datetime
from src.controllers.display_controller import DisplayController

class LoadController:
    """Controller for image loading and processing operations."""
    
    def __init__(self, load_image_widget, sift_widget):
        self.widget = load_image_widget
        self.sift_widget = sift_widget
        self._connect_signals() 
       
    def _connect_signals(self):
        self.widget.btn_load_folder.clicked.connect(self.load_folder)
        self.widget.btn_load_image_l.clicked.connect(self.load_image_l)
        self.widget.btn_load_image_r.clicked.connect(self.load_image_r)
        self.sift_widget.btn_sift_load1.clicked.connect(self.load_image_l)
        self.sift_widget.btn_sift_load2.clicked.connect(self.load_image_r)
    
    def _log_image_info(self, image, file_path, image_type):
        if image is None or (isinstance(image, list) and not image):
            DisplayController.log_message(f"\nError loading {image_type} from {file_path}")
            return        
                
        if image_type == "Folder":
            count = len(image)
            DisplayController.log_message(f"\n[{datetime.now().strftime('%H:%M:%S')}] Loaded {count} images from folder: {file_path}")
            DisplayController.set_images(image)
        else:                       
            filename = os.path.basename(file_path)
            size_kb = os.path.getsize(file_path) / 1024 
            DisplayController.log_message(f"\n[{datetime.now().strftime('%H:%M:%S')}] Uploaded {image_type}: {filename} {size_kb:.1f} KB"
            )
            DisplayController.set_images([image])
        
        DisplayController.set_global_images(image_type, image)
            
    def load_folder(self, specific_path=None):
        """Load a folder of images."""
        if specific_path:
            folder_path = specific_path
        else:
            folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
            
        if folder_path:
            images = []
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    images.append(cv2.imread(file_path))
            self._log_image_info(images, file_path, "Folder")
            
    def load_image_l(self):
        """Load left image."""
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Left Image")
        if file_path:
            image = cv2.imread(file_path)
            self._log_image_info(image, file_path, "Left Image")
            
    def load_image_r(self):
        """Load right image."""
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Right Image")
        if file_path:
            image = cv2.imread(file_path)
            self._log_image_info(image, file_path, "Right Image")
            