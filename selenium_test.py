from selenium import webdriver
from pyvirtualdisplay import Display

# Usar Xvfb para ejecutar en entornos sin GUI
display = Display(visible=0, size=(1920, 1080))
display.start()

# Configurar el driver de Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Prueba: Abrir Google y verificar el título
driver.get("https://www.google.com")
assert "Google" in driver.title

driver.quit()
display.stop()
