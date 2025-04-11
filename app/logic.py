from .config import MAGNIFICATION_FACTOR
from .database import save_record

def calculate_actual_size(microscope_size):
    return microscope_size / MAGNIFICATION_FACTOR

def process_input(username, microscope_size):
    actual_size = calculate_actual_size(microscope_size)
    save_record(username, microscope_size, actual_size)
    return actual_size
