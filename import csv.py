import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Load test data from a CSV file
def load_test_data(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

# Write test results to a CSV file
def log_results(file_path, results):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ["username", "password", "result", "message"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

# Initialize WebDriver
def setup_driver():
    driver = webdriver.Chrome()  # Replace with appropriate WebDriver (e.g., GeckoDriver for Firefox)
    driver.maximize_window()
    return driver

# Perform tests with data and log results
def perform_test(driver, test_data):
    results = []
    for entry in test_data:
        username = entry["username"]
        password = entry["password"]

        try:
            # Open the test URL
            driver.get("http://example.com/login")  # Replace with your application's URL

            # Find and interact with elements
            username_field = driver.find_element(By.NAME, "username")  # Replace with actual locator
            password_field = driver.find_element(By.NAME, "password")  # Replace with actual locator
            login_button = driver.find_element(By.NAME, "login")      # Replace with actual locator

            username_field.clear()
            username_field.send_keys(username)
            password_field.clear()
            password_field.send_keys(password)
            login_button.click()

            # Wait for the result page to load
            time.sleep(2)

            # Check for success condition (update based on your app)
            if "Welcome" in driver.page_source:  # Example success condition
                results.append({"username": username, "password": password, "result": "Pass", "message": "Login successful"})
            else:
                results.append({"username": username, "password": password, "result": "Fail", "message": "Login failed"})
        except Exception as e:
            results.append({"username": username, "password": password, "result": "Error", "message": str(e)})
    
    return results

# Main script
if __name__ == "__main__":
    # Input and output file paths
    input_file_path = "test_data.csv"       # Input file with test data
    output_file_path = "test_results.csv"  # Output file for logging results

    # Load test data
    test_data = load_test_data(input_file_path)

    # Setup WebDriver
    driver = setup_driver()

    try:
        # Execute tests and log results
        test_results = perform_test(driver, test_data)
        log_results(output_file_path, test_results)
        print(f"Test results logged to {output_file_path}")
    finally:
        # Quit WebDriver
        driver.quit()