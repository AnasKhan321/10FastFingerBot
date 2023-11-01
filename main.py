from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver with the correct service and ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Set up the driver for 10fastfingers
def setup_driver():
    driver.implicitly_wait(20)
    # Navigate to a website
    driver.get("https://10fastfingers.com/")


# dissmissing the Pop Up which can cause us error
def dismiss_pop_up():
    pop_up = driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonDecline')
    pop_up.click()


# Entering in to the Typing test Page
def start_typing():
    entrance_button = driver.find_element(By.ID, 'typing-test')
    entrance_button.click()


# Start the Typing with word by word
def type_word_by_word():
    input_element = driver.find_element(By.ID, 'inputfield')

    for i in range(370):
        # taking the current word which we have to written
        text_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'highlight'))
        )
        input_element.send_keys(text_element.text)
        input_element.send_keys(Keys.SPACE)


# Quit the Driver
def quitdriver():
    time.sleep(80)
    driver.quit()


if __name__ == '__main__':
    setup_driver()
    dismiss_pop_up()
    start_typing()
    type_word_by_word()
    quitdriver()
