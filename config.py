"""
config.py
----------------------------------------
Stores application configuration settings
for the Python Lab Assignment.

Author: ______________________
Admission Number: ______________________
"""

# ======================================
# Application Information
# ======================================

APP_NAME = "Python Utility Calculator"
APP_VERSION = "1.0.0"
AUTHOR = "______________________"

# ======================================
# Greeting Settings
# ======================================

DEFAULT_USER = "Student"
WELCOME_MESSAGE = "Welcome to the Python Utility Calculator!"

# ======================================
# Temperature Conversion
# ======================================

CELSIUS_UNIT = "°C"
FAHRENHEIT_UNIT = "°F"

# ======================================
# Input Validation
# ======================================

MIN_NUMBER = -100000
MAX_NUMBER = 100000

# ======================================
# Output Labels
# ======================================

SQUARE_LABEL = "Square"
EVEN_LABEL = "Even Number"
TEMP_LABEL = "Temperature in Fahrenheit"

# ======================================
# Error Messages
# ======================================

INVALID_INPUT = "Error: Please enter a valid numeric value."
OUT_OF_RANGE = (
    f"Error: Number must be between {MIN_NUMBER} and {MAX_NUMBER}."
)

# ======================================
# Git Assignment Information
# ======================================

PROJECT_NAME = "Python Lab Assignment"
PROJECT_STRUCTURE = ["src", "tests", "docs"]
