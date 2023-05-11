import pytest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()

class TestLambdaTestPlayground:
    @pytest.fixture(scope="class")
    def setup(self):
        # Set up the WebDriver instance
        options = Options()
        options.browser_version = "113.0"
        options.platform_name = "Windows 10"
        lt_options = {}
        lt_options["username"] =  os.getenv("EMAIL")
        lt_options["accessKey"] = os.getenv("PASSWORD")
        lt_options["project"] = "Untitled"
        lt_options["w3c"] = True
        lt_options["plugin"] = "python-python"
        lt_options["visual"] = True;
        lt_options["video"] = True;
        lt_options["network"] = True;
        lt_options["build"] = "Testing";
        lt_options["plugin"] = "python-python";
        options.set_capability('LT:Options', lt_options)
        driver = webdriver.Remote(
            command_executor=f'https://{os.getenv("EMAIL")}:{os.getenv("PASSWORD")}@hub.lambdatest.com/wd/hub',
            options=options
        )
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_scenario_1(self, setup):
        driver = setup
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.XPATH, "//a[text()='Simple Form Demo']").click()
        assert "simple-form-demo" in driver.current_url
        message = "Welcome to LambdaTest"
        driver.find_element(By.ID, "user-message").send_keys(message)
        driver.find_element(By.XPATH, "//button[text()='Get Checked value']").click()
        assert message in driver.find_element(By.ID, "message").text

    def test_scenario_2(self, setup):
        driver = setup
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.XPATH, "//a[text()='Drag & Drop Sliders']").click()
        slider = driver.find_element(By.XPATH, "//input[@value='15']")
        driver.execute_script("arguments[0].value = '95';", slider)
        assert slider.get_attribute("value") == "95"

    def test_scenario_3(self, setup):
        driver = setup
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.XPATH, "//a[text()='Input Form Submit']").click()
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        #assert "Please fill out this field" in driver.page_source
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "name"))).send_keys("John")
        driver.find_element(By.XPATH,'(//input[@name="email"])[2]').send_keys("johndoe@example.com")
        driver.find_element(By.NAME,"password").send_keys("1234567890testASD$$")
        driver.find_element(By.NAME,"company").send_keys("Lambda Test")
        driver.find_element(By.NAME, "website").send_keys("lambda.com")
        country_dropdown = Select(driver.find_element(By.NAME,'country'))
        country_dropdown.select_by_visible_text('Andorra')
        driver.find_element(By.NAME, "address_line1").send_keys("1234 Elm Street")
        driver.find_element(By.NAME, "address_line2").send_keys("1234 Elm Street")
        driver.find_element(By.NAME, "city").send_keys("New York")
        driver.find_element(By.ID, "inputState").send_keys("NY")
        driver.find_element(By.NAME, "zip").send_keys("12345")
        element = driver.find_element(By.XPATH, "//button[text()='Submit']")
        driver.execute_script("arguments[0].click();", element)
        assert "Thanks for contacting us, we will get back to you shortly." in WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[text()='Thanks for contacting us, we will get back to you shortly.']"))).text