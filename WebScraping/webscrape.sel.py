from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv 


path  = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path = path)
driver.get("https://es.wikipedia.org/")
search = driver.find_element(By.ID, 'searchInput')
search.send_keys('Dua Lipa')
search_button = driver.find_element(By.ID, 'searchButton')
search_button.click()

# Save information that was found after scraping
def save_information(descripcion_dua):
    filename = 'dualipa.csv'
    with open(filename,'a', newline= '\n') as csvfile:
        fieldnames = ['Edad','Lugar de nacimiento', 'Etnia', 'Lengua materna','Ocupacion','Años activa','Género','Instrumento','Tipo de voz','Sello','sitio web']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow({'Edad':descripcion_dua[1],'Lugar de nacimiento': descripcion_dua[2], 'Etnia':descripcion_dua[3], 'Lengua materna':descripcion_dua[4],'Ocupacion':descripcion_dua[5],'Años activa':descripcion_dua[6],'Género':descripcion_dua[7],'Instrumento':descripcion_dua[8],'Tipo de voz':descripcion_dua[9],'Sello':descripcion_dua[10],'sitio web':descripcion_dua[11]})

# Finds main information from Wikipedia table    
def find():
  descripcion_dua = []
  informacion_completa = driver.find_elements(By.XPATH, '//table[@class="infobox biography vcard"]/tbody/tr/td')
  for i in informacion_completa:
      descripcion_dua.append(i.text)
  return descripcion_dua


informacion =  find()
save_information(informacion)

time.sleep(5)

driver.quit()