import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_template_navigation():
    start_time = time.time()
    driver = None

    try:
        driver = webdriver.Edge(service=Service("msedgedriver.exe"))
        wait = WebDriverWait(driver, 15)

        driver.get("https://invitationnation.in/")
        print("Website opened.")

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[normalize-space()='Invitations']]")
            )
        ).click()
        print("Invitations section opened.")

        links = wait.until(
            lambda d: d.find_elements(
                By.CSS_SELECTOR, 'a[href="/invitations/festivities"]'
            )
        )
        print(f"Festivities links found: {len(links)}")

        link = links[0]
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", link
        )
        link.click()

        wait.until(EC.url_contains("/invitations/festivities"))
        print("Festivities category selected.")
        print("Festivities page opened.")
        print("Current URL:", driver.current_url)

        cards = wait.until(
            lambda d: d.find_elements(By.CSS_SELECTOR, "a.collection-card-link")
        )
        print(f"Template cards found: {len(cards)}")
        assert cards, "No template cards were found."

        selected = cards[0]
        print("Selected template URL:", selected.get_attribute("href"))

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", selected
        )
        selected.click()

        wait.until(EC.url_contains("/invitations/festivities/"))
        print("Template page opened.")
        print("Template page URL:", driver.current_url)
        print("Page title:", driver.title)
        print("STEP 3: PASS")

    except Exception as error:
        print("STEP 3: FAIL")
        print(f"Failure reason: {error}")
        raise

    finally:
        print(f"Execution time: {time.time() - start_time:.2f} seconds")
        if driver:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    test_template_navigation()
