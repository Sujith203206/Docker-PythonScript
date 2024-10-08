# -*- coding: utf-8 -*-
"""Application Health Checker Script.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BnpLqbPDjrVthqNchMYF0NKtUe4YRov2
"""

import requests
import logging
import time

# Setup logging
logging.basicConfig(filename='app_health_check.log',
                    format='%(asctime)s - %(message)s',
                    level=logging.INFO)

# URL of the application to monitor
APP_URL = "https://example.com"  # Replace with the actual URL of our application

# Frequency of checks in seconds
CHECK_INTERVAL = 300  # 5 minute

# Function to check the application's HTTP status
def check_application_status():
    try:
        response = requests.get(APP_URL, timeout=10)  # 10 seconds timeout for a response

        # Check response status code
        if 200 <= response.status_code < 300:
            logging.info(f"Application is UP. Status Code: {response.status_code}")
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status Code: {response.status_code}")
            print(f"Application is DOWN. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # If there is any exception (timeout, connection error, etc.), consider the app down
        logging.error(f"Application is DOWN. Error: {e}")
        print(f"Application is DOWN. Error: {e}")

# Main function to continuously monitor the application
def monitor_application():
    while True:
        check_application_status()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_application()
