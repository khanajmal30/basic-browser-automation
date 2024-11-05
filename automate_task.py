from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Set up the WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Function to automate the repetitive task
def automate_task(username, password):
    try:
        # Navigate to the website
        driver.get('https://www.example.com/login')

        # Find the username and password input elements
        username_input = driver.find_element_by_name('username')
        password_input = driver.find_element_by_name('password')

        # Enter the credentials
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        # Wait for the page to load
        time.sleep(5)

        # Perform the repetitive task
        for i in range(10):
            try:
                # Example task: Click a button
                button = driver.find_element_by_id('button_id')
                button.click()
            except NoSuchElementException:
                print(f"Button not found on iteration {i+1}")
            # Wait for some time before the next iteration
            time.sleep(2)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Close the browser
        driver.quit()

# Function to run all tests
def run_tests():
    # Test cases
    test_cases = [
        {'username': 'correct_username', 'password': 'correct_password', 'expected': True},
        {'username': '', 'password': 'correct_password', 'expected': False},
        {'username': 'correct_username', 'password': '', 'expected': False},
        {'username': 'incorrect_username', 'password': 'correct_password', 'expected': False},
        {'username': 'correct_username', 'password': 'incorrect_password', 'expected': False},
    ]

    # Run each test case
    for i, test in enumerate(test_cases):
        result = automate_task(test['username'], test['password'])
        assert result == test['expected'], f"Test case {i+1} failed"

    print("All test cases passed!")

# Run the tests
run_tests()
