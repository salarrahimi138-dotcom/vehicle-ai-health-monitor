"""
Vehicle AI Health Monitor Configuration
"""

class Config:
    # Project Information
    PROJECT_NAME = "Vehicle AI Health Monitor"
    PROJECT_VERSION = "1.0.0"
    # Data Sources
    STANDARDS_PATH = None
    ECU_DATA_PATH = None
     # Backend Configuration
    BACKEND_URL = None
    REQUEST_TIMEOUT = 30
    # Logging
    LOG_LEVEL = "DEBUG"
    # Risk Thresholds
    NORMAL_THRESHOLD = 30
    WARNING_THRESHOLD = 70
    CRITICAL_THRESHOLD = 90