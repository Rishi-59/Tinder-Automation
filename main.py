import os
from time import sleep
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

URL = os.environ["URL"]
EMAIL = os.environ["EMAIL"]
PASS = os.environ["PASS"]

def wait_till_visible(t_driver,value,by=By.CLASS_NAME):
    sleep(1)
    WebDriverWait(t_driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )

def scroll_into_view(t_driver, element):
    t_driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        element
    )
    sleep(1)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

login_btn = driver.find_element(By.CLASS_NAME, "btn-tindog-login")
login_btn.click()

original_window = driver.current_window_handle

wait_till_visible(driver, "btn-facebark")

facebark_btn = driver.find_element(By.CLASS_NAME, "btn-facebark")
facebark_btn.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) == 2
)

for window in driver.window_handles:
    driver.switch_to.window(window)
    if 'fb-login' in driver.current_url:
        break

email_input = driver.find_element(By.ID, "email")
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(PASS)

submit_btn = driver.find_element(By.TAG_NAME, "button")
submit_btn.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) == 1
)

driver.switch_to.window(original_window)

for _ in range(3):
    wait_till_visible(driver, "btn-primary")
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

like_count = 0
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

while like_count < 20:
    # Find a fresh element every iteration
    like_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "like-button-container"))
    )

    # Scroll it into view
    scroll_into_view(driver, like_btn)

    # Click it
    like_btn.click()
    like_count += 1

    # Handle match popup if it appears
    try:
        popup = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "match-popup-link"))
        )
        popup.click()
    except:
        pass

print("like count exhausted : ", like_count)
driver.close()