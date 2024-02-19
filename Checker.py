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
import os
import inquirer
import logging
import sqlite3
import getpass
from selenium.common.exceptions import JavascriptException
# Configurar el nivel de registro global
logging.basicConfig(level=logging.WARNING)
# Deshabilitar mensajes de advertencia de WebDriver, urllib3 y otros mensajes irrelevantes
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


# Redirigir la salida de error estándar a nul en sistemas Windows
sys.stderr = open("nul", "w")


# Opciones de Chrome
chrome_options = Options()
chrome_options.add_argument(
    "--log-level=3"
)  # Esto establece el nivel de registro de Chrome a "sin registro"
# chrome_options.add_argument("--headless")  # Asegúrate de que esta línea esté descomentada para ejecutar en modo headless
# chrome_options.add_argument("--disable-gpu")  # Esta opción es necesaria para el modo headless
chrome_options.add_argument("--disable-web-security")
# Ahora puedes pasar las chrome_options al constructor de Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()

derechos_de_autor = "Derechos de autor: (C) 2024 Rizzo. Todos los derechos reservados. Contacto-Telegram: @rizssoo"
tester = "Tester: SSLJosh Contacto-Telegram: @SSLJhos101"
codigo_ascii_charged = """
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░  ░█████╗░██╗░░██╗░█████╗░██████╗░░██████╗░███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔════╝░██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝  ██║░░╚═╝███████║███████║██████╔╝██║░░██╗░█████╗░░██║░░██║
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  ██║░░██╗██╔══██║██╔══██║██╔══██╗██║░░╚██╗██╔══╝░░██║░░██║
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║  ╚█████╔╝██║░░██║██║░░██║██║░░██║╚██████╔╝███████╗██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═════╝░
"""
codigo_ascii_auth = """
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░  ░█████╗░██╗░░░██╗████████╗██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ██╔══██╗██║░░░██║╚══██╔══╝██║░░██║
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝  ███████║██║░░░██║░░░██║░░░███████║
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  ██╔══██║██║░░░██║░░░██║░░░██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║  ██║░░██║╚██████╔╝░░░██║░░░██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
"""
codigo_ascii_checker = """
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

#def obtener_usuario_y_contraseña():
#    username = input("Usuario: ")
#    password = getpass.getpass("Contraseña: ")
#    return username, password


#def verificar_usuario(username, password):
#    # Conectar a la base de datos
#    conn = sqlite3.connect('usuarios.db')
#    c = conn.cursor()
#
#    # Verificar el usuario
#    c.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
#    result = c.fetchone()
#
#    # Cerrar la conexión
#    conn.close()
#
#    if result:
#        return True
#    else:
#        return False
    
def execute_script_click_no_bucle(driver, script, additional_delay=0.5):
    try:
        driver.execute_script(script)
        time.sleep(additional_delay)  # Pausa adicional después de ejecutar el script
        return True
    except JavascriptException:
        pass

def css_click_no_bucle(driver, selector, by=By.CSS_SELECTOR, delay_between_attempts=0.3):
    try:
        element = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((by, selector))
        )
        element.click()
        # Verificar que el clic se haya realizado correctamente
        # Puedes agregar condiciones adicionales según la lógica de la página
        # En este ejemplo, solo se verifica si el elemento aún está clickeable después del clic
        WebDriverWait(driver, 4).until_not(EC.element_to_be_clickable((by, selector)))
    except TimeoutException:
        pass
    time.sleep(delay_between_attempts)

def xpath_click_no_bucle(driver, xpath, delay_between_attempts=0.3):
    try:
        WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()
    except (TimeoutException, NoSuchElementException, TypeError):
        pass  # Ignorar la excepción de tiempo de espera
    time.sleep(delay_between_attempts)







def execute_script_click(driver, script, delay_between_attempts=0.5, additional_delay=0.5):
    while True:
        try:
            driver.execute_script(script)
            time.sleep(additional_delay)  # Pausa adicional después de ejecutar el script
            return True
        except JavascriptException:
            time.sleep(delay_between_attempts)



def css_click(driver, selector, by=By.CSS_SELECTOR, delay_between_attempts=1):
    while True:
        try:
            element = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((by, selector))
            )
            element.click()

            # Verificar que el clic se haya realizado correctamente
            # Puedes agregar condiciones adicionales según la lógica de la página
            # En este ejemplo, solo se verifica si el elemento aún está clickeable después del clic
            WebDriverWait(driver, 4).until_not(EC.element_to_be_clickable((by, selector)))
            
            return True

        except TimeoutException:
            time.sleep(delay_between_attempts)



def enter_input_field(driver, selector, input_text, by=By.ID, delay=0.2, timeout=4):
    while True:
        try:
            # Esperar a que el elemento input sea localizable por su selector y luego obtenerlo
            input_field = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )

            input_field.clear()

            # Verificar si el selector es "secCode" para decidir si aplicar el formato
            if selector != "secCode" or selector != '//input[@name="cvc"]':
                # Limpiar texto de entrada de espacios y /
                cleaned_input_text = ''.join(c for c in input_text if c.isdigit())
                input_text_combined = cleaned_input_text.replace(" ", "").replace("/", "").strip()

                # Modificar el formato si la longitud es de MM/YY
                if len(cleaned_input_text) == 4:
                    input_text_combined = cleaned_input_text[:2] + "/" + cleaned_input_text[2:]
            else:
                # No aplicar formato si el selector es "secCode"
                input_text_combined = input_text.strip()

            input_field.send_keys(input_text_combined)

            # Verificar que el texto se haya ingresado correctamente
            entered_text = input_field.get_attribute("value").replace(" ", "").strip()
            if entered_text == input_text_combined:
                return True
        except TimeoutException:
            pass

        time.sleep(delay)






def enter_text_CSS(driver, selector, text, by=By.CSS_SELECTOR):
    try:
        time.sleep(0.5)
        element = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((by, selector))
        )
        element.clear()
        element.send_keys(text)

        # Verificar que el texto se haya ingresado correctamente
        entered_text = element.get_attribute("value")
        if entered_text == text:
            return True
        else:
            # Si el texto no se ingresó correctamente, intentar nuevamente
            element.clear()
            element.send_keys(text)
            entered_text = element.get_attribute("value")
            if entered_text == text:
                return True
            else:
                return False

    except TimeoutException:
        return False
    

def enter_text_xpath(driver, selector, text, by=By.XPATH):
    try:
        time.sleep(0.3)
        element = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((by, selector))
        )
        element.clear()
        element.send_keys(text)

        # Verificar que el texto se haya ingresado correctamente
        entered_text = element.get_attribute("value")
        if entered_text == text:
            return True
        else:
            # Si el texto no se ingresó correctamente, intentar nuevamente
            element.clear()
            element.send_keys(text)
            entered_text = element.get_attribute("value")
            if entered_text == text:
                return True
            else:
                return False

    except TimeoutException:
        return False

def wait_for_element(driver, selector, condition, timeout=4):
    try:
        element = WebDriverWait(driver, timeout).until(
            condition((By.XPATH, selector))
        )
        return element
    except TimeoutException:
        pass
    
def xpath_click(driver, xpath, delay_between_attempts=1):
    while True:
        try:
            element = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()

            # Esperar a que el elemento ya no sea clickeable (se ha realizado el clic)
            WebDriverWait(driver, 4).until_not(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            return True
        except (TimeoutException, NoSuchElementException, TypeError):
            continue

        time.sleep(delay_between_attempts)



def switch_to_frame(driver, locator, by=By.ID, timeout=4):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        driver.switch_to.frame(locator)
        return True
    except TimeoutException:
        return False

def mensaje(message, color_code):
    colored_message = f"\033[{color_code}m{message}\033[0m"
    print(" " * 110, end='\r')
    print(colored_message, end='\r', flush=True)

# Códigos de colores ANSI
COLOR_RED = '91'
COLOR_GREEN = '92'
COLOR_YELLOW = '93'

def seleccionar_tipo(checker):

    if checker == "menu":
        questions = [
            inquirer.List('option',
                          message="Elige tipo de Checker",
                          choices=['Charged', 'Auth'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers['option']

    if checker == "Charged":
        questions = [
            inquirer.List('type',
                          message="Elige una opción",
                          choices=['Express $16.79', 'Express $16.58'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        type_mapping = {
            'Express $16.79': '16.79',
            'Express $16.58': '16.58',
        }
        return type_mapping[answers['type']]
    
    if checker == "auth":
        questions = [
            inquirer.List('type',
                          message="Elige una opción",
                          choices=['Braint', 'xd'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        return answers['type']

def express(card, date, cvv, type):
    urls_messages = {
        "16.79": [
            ("https://www.express.com/clothing/men/floral-dress-socks/pro/04620102/color/Pitch%20Black/", "16.79"),
            ("https://www.express.com/clothing/men/green-clover-dress-socks/pro/04620106/color/ICED%20AQUA/", "16.79"),
            ("https://www.express.com/clothing/men/striped-dress-socks/pro/04620101/color/NAVY/", "16.79")

            # Agrega más tuplas URL-mensaje aquí
        ],
        "16.58": [
            ("https://www.express.com/clothing/women/upwest-cozy-leopard-socks/pro/80157165/color/ANIMAL%20PRINT/", "16.58"),
            # Agrega más tuplas URL-mensaje aquí
        ],
        # Agrega más listas de URLs aquí
    }

    urls_messages_selected = urls_messages[type] if type in urls_messages else list(urls_messages.values())[0]

    success = False  # Inicializa la variable de control
    for url, message in urls_messages_selected:

        if success:  # Si la variable de control es True, rompe el bucle for
            break
        start_time = time.time()  # Guarda el tiempo de inicio
        try:
            while True:
                mensaje(f"${type} Url: ${url}", COLOR_YELLOW)
                mensaje(f"Procesando...", COLOR_YELLOW)
                driver.get(url)

                try:
                   css_click_no_bucle(driver, "button.fsrButton.fsrButton__inviteDecline.fsrDeclineButton")
                except NoSuchElementException:
                    pass
            
                try: #CERRAR COOKIES
                    execute_script_click_no_bucle(driver, "document.querySelector('.onetrust-close-btn-handler').click();")
                    execute_script_click_no_bucle(driver, "document.querySelector('.onetrust-close-btn-handler').click();")
                    mensaje("Se cerraron las cookies correctamente.", COLOR_YELLOW)
                except JavascriptException:
                    mensaje("Hubo un error al tratar de cerrar las cookies.", COLOR_RED)
            
                try: #AÑADIR AL CARRITO
                    mensaje("Añadiendo al carrito...", COLOR_YELLOW)
                    execute_script_click(driver, "document.querySelector(\"button[unbxdattr='AddToCart']\").click();")
                    mensaje("Se añadió al carrito correctamente.", COLOR_YELLOW)
                except JavascriptException:
                    mensaje("Hubo un error al tratar de añadir al carrito.", COLOR_RED)
            
                driver.get("https://www.express.com/checkout/contact-information")
                try:
                    # Intenta encontrar y hacer clic en el botón 'No thanks' si está presente
                    css_click_no_bucle(driver, "button.fsrButton.fsrButton__inviteDecline.fsrDeclineButton")
                    mensaje("Colocando información...", COLOR_YELLOW)
                except NoSuchElementException as e:
                    pass
                
                try: #CERRAR COOKIES
                    execute_script_click_no_bucle(driver, "document.querySelector('.onetrust-close-btn-handler').click();")
                except JavascriptException:
                    mensaje("Hubo un error al tratar de cerrar las cookies.", COLOR_RED)
    
    
                time.sleep(0.2)
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ YMB2H' and @id='contact-information-firstname']", "dsadsad")
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ YMB2H' and @id='contact-information-lastname']", "dsadsad")
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ mBaDI' and @id='contact-information-email']", "dawdwafafw@gmail.com")
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ mBaDI' and @id='contact-information-confirmemail']", "dawdwafafw@gmail.com")
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ r3Bel' and @id='contact-information-phone']", "(213) 231-2321")
                time.sleep(0.3)
        
                try:
                    xpath_click_no_bucle(driver, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT XeI2t' and not(@aria-label)]")
                except NoSuchElementException:
                    mensaje("Hubo un error al tratar de dar click en el boton de Info contacto.", COLOR_RED)
        
                time.sleep(0.3)
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ QmZ+J' and @id='shipping.line1']", "dwqdqwfqwfqwfqw")
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ n9hK0' and @id='shipping.postalCode']", "231232")
                enter_text_xpath(driver, "//input[@class='C-KSdhEJ vwtDb' and @id='shipping.city']", "dawdsaf")
                time.sleep(0.3)
        
                try:
                    xpath_click_no_bucle(driver, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT Rpw9i' and not(@aria-label)]")
                    xpath_click_no_bucle(driver, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT Rpw9i' and not(@aria-label)]")
                except NoSuchElementException:
                    mensaje("Hubo un error al tratar de dar click en el boton de Info de direccion.", COLOR_RED)
                try:
                    xpath_click_no_bucle(driver, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT vX8Q2']")
                    xpath_click_no_bucle(driver, "//button[@class='btn VgwgDBBL i31kbSky a-YwkJU2 _0TgAT vX8Q2']")
                except JavascriptException:
                    mensaje("Hubo un error al tratar de dar click en el boton de Info de envio.", COLOR_RED)
        
        
        
                for _ in range(3):
                    frame = "aurusIframe"
                    if switch_to_frame(driver, frame):
                        enter_input_field(driver, "cNumber", card)
                        enter_input_field(driver, "exDate", date)
                        enter_input_field(driver, "secCode", cvv)
                        driver.switch_to.default_content()
                        mensaje("Datos de tarjeta ingresados!", COLOR_YELLOW)
                        break
                    else:
                        mensaje("No se pudo ingresar al frame", COLOR_RED)
                else:
                    print("\033[93mNo se pudo ingresar al frame después de 3 intentos. Volviendo a intentar...\033[0m", end='\r', flush=True)
                    driver.delete_all_cookies()
                    continue #continua la siguiente iteracion del bucle while
        
                try:
                    execute_script_click(driver, "document.querySelector(\"button.btn.VgwgDBBL.i31kbSky.a-YwkJU2._0TgAT[data-selected='false']\").click();")
                    mensaje("Datos de tarjeta guardados!", COLOR_YELLOW)
                except JavascriptException:
                    mensaje("Hubo un error al tratar de dar click en el boton de guardar.", COLOR_RED)
        
                try:
                    css_click_no_bucle(driver, "button.btn.VgwgDBBL.i31kbSky.a-YwkJU2._0TgAT.p2TWK")
                    css_click_no_bucle(driver, "button.btn.VgwgDBBL.i31kbSky.a-YwkJU2._0TgAT.p2TWK")
                    mensaje("Checking...", COLOR_YELLOW)
                except:
                    mensaje("Hubo un error al tratar de dar click en el boton de Checking.", COLOR_RED)
        
                try:
                    WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//h2[contains(@class, 'lixW-')]")
                        )
                    )
                    elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
    
                    # print("Se encontró el encabezado 'Delivery Details'.")
                    formatted_date = f"{date[:2]}|20{date[2:]}"
                    print(" " * 90, end='\r')
                    print("\033[92m" + f"{card}|{formatted_date}|{cvv}" + "\033[32m" + " ➥  " + "\033[36m" + f"{elapsed_time:.1f}s" + "\033[35m" + " - " + "\033[92m" + f"CHARGED ${message}!" + "\033[0m")
                    driver.delete_all_cookies()

                    success = True  # romper el bucle for de urls si se encuentra el encabezado
                    break # Romper el bucle while si se encuentra el encabezado
                except (TimeoutException, NoSuchElementException):
    
                    elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
                    formatted_date = f"{date[:2]}|20{date[2:]}"
                    print(" " * 90, end='\r')
                    print("\033[91m" + f"{card}|{formatted_date}|{cvv}" + "\033[31m" + " ➥  " + "\033[36m" + f"{elapsed_time:.1f}s" + "\033[0m")                   
                    driver.delete_all_cookies()
                    success = True  # romper el bucle for de urls si se encuentra el encabezado
                    break # Romper el bucle while si no se encuentra el encabezado
        except Exception:  # Puedes especificar el tipo de excepción si lo conoces
            mensaje(f"Ocurrió un error con la URL {url}, intentando con la siguiente...", COLOR_RED)
            continue




def cargar_cards_desde_consola(typeSelected):
    while True:

        if typeSelected == "Charged":
            codigo_ascii = codigo_ascii_charged
        if typeSelected == "Auth":
            codigo_ascii = codigo_ascii_auth
        print("\033[91m" + codigo_ascii + "\033[0m")
        print("\033[93m" + derechos_de_autor + "\033[0m")
        print("\033[93m" + tester + "\n" + "\033[0m")
        print("\033[92mIngrese las tarjetas (formato: Card|MM|AAAA|CVV):\033[0m")
        credenciales = []
        try:
            while True:
                input_line = input().strip()
                if not input_line:
                    break

                partes = input_line.split("|")
                partes = [parte.strip() for parte in partes]

                # Si el formato de la tarjeta es incorrecto
                if len(partes) != 4:
                    print("\033[91mFormato incorrecto. Debe ser 'Card|MM|AAAA|CVV'.\033[0m")
                    time.sleep(2)  # Esperar un segundo
                    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
                    break  # Romper el bucle interno y solicitar nuevamente las tarjetas

                card = partes[0]
                exp_date = partes[1] + partes[2][2:]
                cvv = partes[3]
                credenciales.append((card, exp_date, cvv))

        except KeyboardInterrupt:
            # Manejar la interrupción por teclado (Ctrl+C) para salir limpiamente
            print("\n\033[91mInterrupción por teclado. Saliendo...\033[0m")
            break  # Romper el bucle externo si se presiona Ctrl+C

        if credenciales:
            print("\033[92mTarjetas cargadas correctamente!\033[0m")
            print(" ")
            break  # Romper el bucle externo si las tarjetas se ingresaron correctamente

    return credenciales




def main():
    print("\033[91m" + codigo_ascii_checker + "\033[0m")
    print("\033[93m" + derechos_de_autor + "\033[0m")
    print("\033[93m" + tester + "\n" + "\033[0m")
    option = seleccionar_tipo("menu")
   
    if option == "Charged":
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        credenciales = cargar_cards_desde_consola(option)
        type_selected = seleccionar_tipo("Charged")

        for card, date, cvv in credenciales:
            express(card, date, cvv, type_selected)
            time.sleep(0.5)  # Retardo entre cada intento de inicio de sesión


#if __name__ == "__main__":
#    while True:
#        username, password = obtener_usuario_y_contraseña()
#        if verificar_usuario(username, password):
#            print('Inicio de sesión exitoso')
#            while True: 
#                main()
#                print("Asegure y guarde las tarjetas. ¿Desea continuar o salir? Presione 'c' para continuar, 'q' para salir.")
#                key = msvcrt.getch().decode("utf-8").lower()
#                if key == "q":
#                    sys.exit()
#        else:
#            print('Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.')
#            time.sleep(1)  # Esperar un segundo
#            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola


if __name__ == "__main__":
    while True: 
        main()
        mensaje("Asegure y guarde las tarjetas. ¿Desea continuar o salir? Presione 'c' para continuar, 'q' para salir.", COLOR_YELLOW)
        try:
            key = msvcrt.getch().decode("utf-8").lower()
            if key == "q":
                driver.quit()
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
                sys.exit()
        except UnicodeDecodeError:
            continue  # Ignorar el error y continuar con la siguiente iteración del bucle

        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
