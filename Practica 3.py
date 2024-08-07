#Paso 1: Importar bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Paso #2: Inicialización del driver
driver = webdriver.Chrome()

# Paso 3: Definir URL para el scraping
url = "https://books.toscrape.com/"

# Paso #4: Navegar a la página
driver.get(url)

# Paso 5: Inicializar lista vacía
datos = []

#Extraer datos 
def extraer_datos():
    # Encontrar todos los libros en la página actual
    libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in libros:
        titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        precio = libro.find_element(By.CSS_SELECTOR, "p.price_color").text
        disponibilidad = libro.find_element(By.CSS_SELECTOR, "p.availability").text.strip()
        
        datos.append({
            "Título": titulo,
            "Precio": precio,
            "Disponibilidad": disponibilidad
        })

# Extraer datos de la página actual
extraer_datos()

# Cerrar el navegador
driver.quit()

# Crear DataFrame con los datos extraídos
df = pd.DataFrame(datos)
