from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# Inicializa el navegador web (debes tenerlo instalado en tu sistema)
  # Puedes usar otro navegador como Firefox o Edge cambiando el nombre aquí.

# Abre una página web

nomina: int = "56269"
name  = "DANIEL EDUARDO RUIS LOPEZ"
correo = "eduardo.ruis@procesa.mx"
empresa = "1"
asunto = input("Asunto\n")
servicio = "18"
urgencia = "3"
descripcion = asunto

driver = webdriver.Chrome()
driver.get("https://procesa.app/ayudati.php")
try:
    campo_nomina = driver.find_element_by_id("nomina")
    campo_nombre = driver.find_element_by_id("nombre")
    campo_empresa =driver.find_element_by_id("empresa")
    campo_correo = driver.find_element_by_id("correo")
    campo_asunto = driver.find_element_by_id("asunto")
    campo_servicio =driver.find_element_by_id("servicio")
    campo_urgencia =driver.find_element_by_id("urgencia")
    campo_descripcion = driver.find_element_by_id("descripcion")

    campo_nomina.send_keys(nomina)
    campo_nombre.send_keys(name)

    select = Select(campo_empresa)
    select.select_by_value(empresa) 

    campo_correo.send_keys(correo)


    campo_asunto.send_keys(asunto)

    select = Select(campo_servicio)
    select.select_by_value(servicio) 

    select = Select(campo_urgencia)
    select.select_by_value(urgencia)

    campo_descripcion.send_keys(descripcion)
    print(f"Campo nomina: {campo_nomina}")
except Exception as e:
    print(f"Se produjo un error: {str(e)}")
    
finally:
    driver.quit()

