import os
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_EMAIL = os.getenv("INVITATION_TEST_EMAIL")
TEST_PASSWORD = os.getenv("INVITATION_TEST_PASSWORD")

def test_login_dashboard():
    if not TEST_EMAIL or not TEST_PASSWORD:
        raise RuntimeError("Set INVITATION_TEST_EMAIL and INVITATION_TEST_PASSWORD before running.")

    start_time = time.time()
    driver = None

    try:
        driver = webdriver.Edge(service=Service("msedgedriver.exe"))
        wait = WebDriverWait(driver, 10)

        print("Browser started.")
        driver.get("https://invitationnation.in/")
        print("Invitation Nation opened.")

        original_window = driver.current_window_handle

        wait.until(EC.element_to_be_clickable((By.ID, "user-signin-signup"))).click()
        print("Sign In / Sign Up clicked.")

        wait.until(EC.number_of_windows_to_be(2))
        login_window = next(w for w in driver.window_handles if w != original_window)
        driver.switch_to.window(login_window)
        print("Switched to login tab.")

        email = wait.until(EC.visibility_of_element_located((By.ID, "signin-email")))
        email.clear()
        email.send_keys(TEST_EMAIL)

        password = wait.until(EC.visibility_of_element_located((By.ID, "signin-password")))
        password.clear()
        password.send_keys(TEST_PASSWORD)

        print("Login credentials entered.")

        wait.until(EC.element_to_be_clickable((By.ID, "signin-submit-button"))).click()
        print("Login button clicked.")

        heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Welcome to Invitation Nation']")
            )
        )
        assert heading.is_displayed()

        print("User Dashboard loaded successfully.")
        print("TEST CASE 1: PASS")

    except Exception as error:
        print("TEST CASE 1: FAIL")
        print(f"Failure reason: {error}")
        raise

    finally:
        print(f"Execution time: {time.time() - start_time:.2f} seconds")
        if driver:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    test_login_dashboard()
