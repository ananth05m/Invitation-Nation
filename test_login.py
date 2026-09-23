import time
import requests
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================================================
# TEST DATA
# =========================================================

# Replace these with your actual Invitation Nation login
# credentials that you already used successfully.

TEST_EMAIL = "ananth.mahesh00@gmail.com"
TEST_PASSWORD = "Test@12345"


# Paste your working Google Apps Script Web App URL here.
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzvF9gmCOCSRVXT2PAr4L_UrMip--ikH08OSfI8oK_x2phhtS4shA5r-W3bUmcdDzvT/exec"


# =========================================================
# GOOGLE SHEET LOGGER
# =========================================================

def log_result(timestamp, test_case, status,
               execution_time, failure_reason):

    data = {
        "timestamp": timestamp,
        "test_case": test_case,
        "status": status,
        "execution_time": execution_time,
        "failure_reason": failure_reason
    }

    response = requests.post(
        GOOGLE_SCRIPT_URL,
        json=data,
        timeout=30
    )

    response.raise_for_status()

    print("Google Sheet logging completed.")
    print("Google response:", response.text)


# =========================================================
# TEST CASE 1
# LOGIN AND USER DASHBOARD
# =========================================================

def test_login_dashboard():

    print("\n========================================")
    print("TEST CASE 1")
    print("========================================")

    test_case = "Test Case 1 - Login and User Dashboard"

    start_time = time.time()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    driver = None

    status = "FAIL"
    failure_reason = ""

    try:

        # -------------------------------------------------
        # START EDGE
        # -------------------------------------------------

        service = Service("msedgedriver.exe")

        driver = webdriver.Edge(
            service=service
        )

        wait = WebDriverWait(driver, 15)

        print("Browser started.")

        # -------------------------------------------------
        # OPEN INVITATION NATION
        # -------------------------------------------------

        driver.get(
            "https://invitationnation.in/"
        )

        print("Invitation Nation opened.")

        # Store original browser tab
        original_window = driver.current_window_handle

        # -------------------------------------------------
        # CLICK SIGN IN / SIGN UP
        # -------------------------------------------------

        sign_in_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "user-signin-signup"
                )
            )
        )

        sign_in_button.click()

        print("Sign In / Sign Up clicked.")

        # -------------------------------------------------
        # WAIT FOR LOGIN TAB
        # -------------------------------------------------

        wait.until(
            EC.number_of_windows_to_be(2)
        )

        login_window = next(
            window
            for window in driver.window_handles
            if window != original_window
        )

        driver.switch_to.window(
            login_window
        )

        print("Switched to login tab.")

        # -------------------------------------------------
        # ENTER EMAIL
        # -------------------------------------------------

        email_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.ID,
                    "signin-email"
                )
            )
        )

        email_field.clear()

        email_field.send_keys(
            TEST_EMAIL
        )

        # -------------------------------------------------
        # ENTER PASSWORD
        # -------------------------------------------------

        password_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.ID,
                    "signin-password"
                )
            )
        )

        password_field.clear()

        password_field.send_keys(
            TEST_PASSWORD
        )

        print("Login credentials entered.")

        # -------------------------------------------------
        # CLICK LOGIN
        # -------------------------------------------------

        login_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "signin-submit-button"
                )
            )
        )

        login_button.click()

        print("Login button clicked.")

        # -------------------------------------------------
        # VERIFY USER DASHBOARD
        # -------------------------------------------------

        dashboard_heading = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h2[normalize-space()='Welcome to Invitation Nation']"
                )
            )
        )

        assert dashboard_heading.is_displayed(), (
            "User Dashboard heading is not displayed."
        )

        print("User Dashboard loaded successfully.")

        # -------------------------------------------------
        # TEST PASSED
        # -------------------------------------------------

        status = "PASS"

        print("TEST CASE 1: PASS")

    except Exception as error:

        # -------------------------------------------------
        # TEST FAILED
        # -------------------------------------------------

        status = "FAIL"

        failure_reason = str(error)

        print("TEST CASE 1: FAIL")
        print("Failure reason:", failure_reason)

    finally:

        # -------------------------------------------------
        # CALCULATE EXECUTION TIME
        # -------------------------------------------------

        execution_time = time.time() - start_time

        execution_time_text = (
            f"{execution_time:.2f} seconds"
        )

        print(
            "Execution time:",
            execution_time_text
        )

        # -------------------------------------------------
        # LOG RESULT
        # -------------------------------------------------

        try:

            log_result(
                timestamp,
                test_case,
                status,
                execution_time_text,
                failure_reason
            )

        except Exception as logging_error:

            print(
                "WARNING: Google Sheet logging failed."
            )

            print(
                "Logging error:",
                logging_error
            )

        # -------------------------------------------------
        # CLOSE BROWSER
        # -------------------------------------------------

        if driver:

            driver.quit()

            print("Browser closed.")


# =========================================================
# TEST CASE 2
# INVITATION TEMPLATE LIVE DEMO
# =========================================================

def test_case_2_live_demo():

    print("\n========================================")
    print("TEST CASE 2")
    print("========================================")

    test_case = "Test Case 2 - Invitation Template Live Demo"

    start_time = time.time()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    driver = None

    status = "FAIL"
    failure_reason = ""

    try:

        # -------------------------------------------------
        # START EDGE
        # -------------------------------------------------

        service = Service("msedgedriver.exe")

        driver = webdriver.Edge(
            service=service
        )

        wait = WebDriverWait(driver, 15)

        print("Browser started.")

        # -------------------------------------------------
        # OPEN WEBSITE
        # -------------------------------------------------

        driver.get(
            "https://invitationnation.in/"
        )

        print("Website opened.")

        # Store original browser tab
        original_window = driver.current_window_handle

        # -------------------------------------------------
        # OPEN INVITATIONS SECTION
        # -------------------------------------------------

        invitations_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[.//span[normalize-space()='Invitations']]"
                )
            )
        )

        invitations_button.click()

        print("Invitations section opened.")

        # -------------------------------------------------
        # FIND FESTIVITIES CATEGORY
        # -------------------------------------------------

        festivities_links = wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    "a[href='/invitations/festivities']"
                )
            )
        )

        print(
            "Festivities links found:",
            len(festivities_links)
        )

        assert len(festivities_links) > 0, (
            "Festivities category link was not found."
        )

        festivities_category = festivities_links[0]

        print(
            "Festivities URL:",
            festivities_category.get_attribute("href")
        )

        # -------------------------------------------------
        # SELECT FESTIVITIES CATEGORY
        # -------------------------------------------------

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            festivities_category
        )

        driver.execute_script(
            "arguments[0].click();",
            festivities_category
        )

        print("Festivities category selected.")

        # -------------------------------------------------
        # VERIFY CATEGORY PAGE
        # -------------------------------------------------

        wait.until(
            EC.url_contains(
                "/invitations/festivities"
            )
        )

        print("Festivities page opened.")

        # -------------------------------------------------
        # FIND TEMPLATE CARDS
        # -------------------------------------------------

        template_cards = wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    "a.collection-card-link"
                )
            )
        )

        print(
            "Template cards found:",
            len(template_cards)
        )

        assert len(template_cards) > 0, (
            "No invitation templates were found."
        )

        # Select first template
        selected_template = template_cards[0]

        selected_template_url = (
            selected_template.get_attribute("href")
        )

        print(
            "Selected template:",
            selected_template_url
        )

        # -------------------------------------------------
        # SELECT TEMPLATE
        # -------------------------------------------------

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            selected_template
        )

        driver.execute_script(
            "arguments[0].click();",
            selected_template
        )

        print("Template selected.")

        # -------------------------------------------------
        # VERIFY TEMPLATE PAGE
        # -------------------------------------------------

        wait.until(
            lambda d: d.current_url !=
            "https://invitationnation.in/invitations/festivities"
        )

        print("Template page opened.")

        print(
            "Template URL:",
            driver.current_url
        )

        # -------------------------------------------------
        # FIND LIVE DEMO BUTTON
        # -------------------------------------------------

        live_demo_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "button.demo-live-btn"
                )
            )
        )

        assert live_demo_button.is_displayed(), (
            "Live Demo button is not displayed."
        )

        print("Live Demo button found.")

        # -------------------------------------------------
        # STORE EXISTING WINDOWS
        # -------------------------------------------------

        old_windows = set(
            driver.window_handles
        )

        # -------------------------------------------------
        # CLICK LIVE DEMO
        # -------------------------------------------------

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            live_demo_button
        )

        driver.execute_script(
            "arguments[0].click();",
            live_demo_button
        )

        print("Live Demo clicked.")

        # -------------------------------------------------
        # WAIT FOR NEW DEMO TAB
        # -------------------------------------------------

        wait.until(
            lambda d:
            len(d.window_handles) > len(old_windows)
        )

        new_windows = (
            set(driver.window_handles)
            - old_windows
        )

        print(
            "New windows detected:",
            len(new_windows)
        )

        assert len(new_windows) == 1, (
            f"Expected exactly one new demo tab, "
            f"but found {len(new_windows)}."
        )

        demo_window = new_windows.pop()

        print("New demo tab opened.")

        # -------------------------------------------------
        # SWITCH TO DEMO TAB
        # -------------------------------------------------

        driver.switch_to.window(
            demo_window
        )

        print("Switched to demo tab.")

        # -------------------------------------------------
        # WAIT FOR DEMO PAGE TO LOAD
        # -------------------------------------------------

        wait.until(
            lambda d:
            d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        print("Demo page finished loading.")

        # -------------------------------------------------
        # VERIFY LIVE DEMO PAGE
        # -------------------------------------------------

        demo_url = driver.current_url
        demo_title = driver.title

        print(
            "Demo URL:",
            demo_url
        )

        print(
            "Demo title:",
            demo_title
        )

        # Verify expected Live Demo URL
        assert "livedemo.invitationnation.in" in demo_url, (
            f"Unexpected Live Demo URL: {demo_url}"
        )

        # Verify expected page title
        assert "Invitation Nation" in demo_title, (
            f"Unexpected page title: {demo_title}"
        )

        # Verify major page element
        body = wait.until(
            EC.visibility_of_element_located(
                (
                    By.TAG_NAME,
                    "body"
                )
            )
        )

        assert body.is_displayed(), (
            "Live Demo page body is not displayed."
        )

        print(
            "Live Demo page verified successfully."
        )

        # -------------------------------------------------
        # CLOSE DEMO TAB
        # -------------------------------------------------

        driver.close()

        print("Demo tab closed.")

        # -------------------------------------------------
        # RETURN TO ORIGINAL TAB
        # -------------------------------------------------

        driver.switch_to.window(
            original_window
        )

        assert (
            driver.current_window_handle
            == original_window
        )

        print(
            "Successfully returned to original tab."
        )

        # -------------------------------------------------
        # TEST PASSED
        # -------------------------------------------------

        status = "PASS"

        print("TEST CASE 2: PASS")

    except Exception as error:

        # -------------------------------------------------
        # TEST FAILED
        # -------------------------------------------------

        status = "FAIL"

        failure_reason = str(error)

        print("TEST CASE 2: FAIL")
        print("Failure reason:", failure_reason)

    finally:

        # -------------------------------------------------
        # CALCULATE EXECUTION TIME
        # -------------------------------------------------

        execution_time = time.time() - start_time

        execution_time_text = (
            f"{execution_time:.2f} seconds"
        )

        print(
            "Execution time:",
            execution_time_text
        )

        # -------------------------------------------------
        # LOG RESULT
        # -------------------------------------------------

        try:

            log_result(
                timestamp,
                test_case,
                status,
                execution_time_text,
                failure_reason
            )

        except Exception as logging_error:

            print(
                "WARNING: Google Sheet logging failed."
            )

            print(
                "Logging error:",
                logging_error
            )

        # -------------------------------------------------
        # CLOSE BROWSER
        # -------------------------------------------------

        if driver:

            driver.quit()

            print("Browser closed.")


# =========================================================
# RUN BOTH TEST CASES
# =========================================================

if __name__ == "__main__":

    test_login_dashboard()

    test_case_2_live_demo()