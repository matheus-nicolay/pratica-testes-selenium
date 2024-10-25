from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
import chromedriver_binary
import time
import os

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

relative_path = './sample-exercise.html'
absolute_path = os.path.abspath(relative_path)
absolute_path = absolute_path.replace("\\", "/")

driver.get(f'file:///{absolute_path}')
print("Página carregada.")

generate_button = driver.find_element(By.NAME, "generate")
generate_button.click()

# Aguarda o código ser gerado
time.sleep(5) 

# Capture o código gerado
generated_code = driver.find_element(By.ID, "my-value").text
print(f"Generated code: {generated_code}")

# Preencha o campo de texto com o código gerado
input_field = driver.find_element(By.ID, "input")
input_field.clear() 
input_field.send_keys(generated_code)
test_button = driver.find_element(By.NAME, "button")
test_button.click()

# Manipula o alerta exibido
alert = Alert(driver)
alert_text = alert.text
print(f"Alert text: {alert_text}")
alert.accept() 

# Verifica a mensagem exibida
result_text = driver.find_element(By.ID, "result").text
expected_text = f"It workls! {generated_code}!"

if result_text == expected_text:
    print("Test passed: The result message is correct!")
else:
    print(f"Test failed: Expected '{expected_text}', but got '{result_text}'")

# Fecha o navegador
driver.quit()