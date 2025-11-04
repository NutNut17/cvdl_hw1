from PyQt5.QtCore import QObject
from datetime import datetime

class DisplayController(QObject):
    
    _display = None
    _global_images = {}
    _images = {}
    _current_index = 0
    
    @classmethod
    def initialize(cls, display_widget):
        """Initialize the singleton instance."""
        if cls._display is None:
            cls._display = display_widget
            
            
    def __init__(self):
        """Protected constructor - use DisplayController.initialize() instead."""
        super().__init__()        
        
    @classmethod
    def get_global_images(cls, category):
        if category in cls._global_images:
            return cls._global_images[category].copy()
        else:
            return None
    
    @classmethod
    def set_global_images(cls, category, images):
        cls._global_images[category] = images
    
    @classmethod
    def set_images(cls, images):
        cls._images = images
        cls._current_index = 0
        cls.display_image(cls._images[cls._current_index])

    @classmethod
    def log_message(cls, message):
        cls._display.log_message(f"\n[{datetime.now().strftime('%H:%M:%S')}] {message}")

    @classmethod
    def display_image(cls, image):
        cls._display.display_image(image)
    
    @classmethod
    def show_next_image(cls):
        if not cls._images:
            cls.log_message("No images loaded.")
            return
        cls._current_index = (cls._current_index + 1) % len(cls._images)
        cls.display_image(cls._images[cls._current_index])

    @classmethod
    def show_prev_image(cls):
        if not cls._images:
            cls.log_message("No images loaded.")
            return
        cls._current_index = (cls._current_index - 1) % len(cls._images)
        cls.display_image(cls._images[cls._current_index])