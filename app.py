from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://automatize.netlify.app/')
sleep(5)

campo_usuario = driver.find_element(By.XPATH,"//input[@id='email']")
campo_senha = driver.find_element(By.XPATH,"//input[@id='senha']")

campo_usuario.send_keys('welbeneskenedy@gmail.com')
sleep(2)
campo_senha.send_keys('81510063')
sleep(2)

botao_login = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
sleep(1)
botao_login.click()



input('')



