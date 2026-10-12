from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    driver.get("http://localhost:3000/")

    # FUNCTIONALITY TEST: CREATE
    name = "TestStudent" + datetime.now().strftime("%H%M%S")
    department = "CSE"

    name_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter student name']")
        )
    )
    name_input.send_keys(name)

    driver.find_element(
        By.XPATH, "//input[@placeholder='Enter department']"
    ).send_keys(department)

    driver.find_element(
        By.XPATH, "//form[.//button[contains(., 'Register Student')]]//button[@type='submit']"
    ).click()

    try:
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".message"),
                "Student registered successfully!"
            )
        )
    except TimeoutException:
        print("Registration message:", driver.find_element(
            By.CSS_SELECTOR, ".message"
        ).text)
        print("Error message:", driver.find_element(
            By.CSS_SELECTOR, ".error"
        ).text)
        raise Exception(
            "Registration did not succeed. Check the backend and MongoDB."
        )

    print("PASS: CREATE - Student registered")

    # FUNCTIONALITY TEST: READ
    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"), name
        )
    )
    print("PASS: READ - Student displayed")

    # UI TEST
    assert driver.find_element(By.TAG_NAME, "h2").is_displayed()
    assert driver.find_element(
        By.XPATH, "//button[contains(., 'Edit')]"
    ).is_displayed()
    assert driver.find_element(
        By.XPATH, "//button[contains(., 'Delete')]"
    ).is_displayed()

    print("PASS: UI - Heading and action buttons visible")

    # USABILITY TEST
    assert driver.find_element(
        By.XPATH, "//input[@placeholder='Enter student name']"
    ).is_displayed()
    assert driver.find_element(
        By.XPATH, "//input[@placeholder='Enter department']"
    ).is_displayed()

    print("PASS: USABILITY - Input fields are visible")

    # FUNCTIONALITY TEST: UPDATE
    student_row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[contains(., '" + name + "')]")
        )
    )

    student_row.find_element(
        By.XPATH, ".//button[contains(., 'Edit')]"
    ).click()

    edit_name = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@ng-if='editingStudent']//input[1]")
        )
    )
    edit_name.clear()
    edit_name.send_keys(name + "Updated")

    edit_department = driver.find_element(
        By.XPATH, "//div[@ng-if='editingStudent']//input[2]"
    )
    edit_department.clear()
    edit_department.send_keys("IT")

    driver.find_element(
        By.XPATH, "//button[contains(., 'Save Changes')]"
    ).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".message"),
            "Student updated successfully!"
        )
    )

    print("PASS: UPDATE - Student updated")

    # FUNCTIONALITY TEST: DELETE
    updated_name = name + "Updated"

    updated_row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[contains(., '" + updated_name + "')]")
        )
    )

    updated_row.find_element(
        By.XPATH, ".//button[contains(., 'Delete')]"
    ).click()

    wait.until(EC.staleness_of(updated_row))

    print("PASS: DELETE - Student deleted")
    print("\\nALL SELENIUM TESTS PASSED!")

except Exception as error:
    print("TEST FAILED:", repr(error))
    raise

finally:
    driver.quit()
