"""
config.py

Configuration settings for the Python Lab Assignment.
This file stores constants used throughout the application.
"""

# ==========================================
# Application Information
# ==========================================

APP_NAME = "Python Utility Calculator"
APP_VERSION = "1.0"
AUTHOR = "Your Name"

# ==========================================
# Default Settings
# ==========================================

DEFAULT_USER = "Student"

# ==========================================
# Number Limits
# ==========================================

MIN_NUMBER = -100000
MAX_NUMBER = 100000

# ==========================================
# Temperature Conversion
# ==========================================

CELSIUS_UNIT = "°C"
FAHRENHEIT_UNIT = "°F"

# ==========================================
# Output Labels
# ==========================================

SQUARE_LABEL = "Square"
EVEN_LABEL = "Even"
FAHRENHEIT_LABEL = "Temperature (°F)"

# ==========================================
# Messages
# ==========================================

WELCOME_MESSAGE = "Welcome to the Python Utility Calculator!"
GOODBYE_MESSAGE = "Thank you for using the program."

INVALID_INPUT = "Invalid input. Please enter a valid number."
OUT_OF_RANGE = (
    f"Number must be between {MIN_NUMBER} and {MAX_NUMBER}."
)
