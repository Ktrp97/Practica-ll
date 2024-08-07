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
    libros = driver.find_elements(By.CLASS_NAME, "product_pod")
    for libro in libros:
        # Extraer el título del libro
        titulo_elemento = libro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        titulo = titulo_elemento.get_attribute("title")
        
        # Extraer el precio del libro
        precio = libro.find_element(By.CLASS_NAME, "price_color").text
        
        # Extraer la disponibilidad del libro
        disponibilidad = libro.find_element(By.CLASS_NAME, "availability").text.strip()
        
# Agregar los datos
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
