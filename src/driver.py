import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.config import HEADLESS_MODE

def get_driver():
    """
    Inicializa el navegador Chrome con configuración de perfil persistente.
    Permite mantener la sesión iniciada entre ejecuciones.
    """
    print("🚗 Inicializando navegador con perfil persistente...")
    
    # Configuración de la ruta del perfil de usuario local.
    # Siempre usa la carpeta 'profile' dentro del proyecto.
    base_dir = os.getcwd()
    profile_dir = os.path.join(base_dir, "profile")
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
        print(f"   -> Creando perfil local (bot dedicado) en: {profile_dir}")
    else:
        print(f"   -> Usando perfil local en: {profile_dir}")

    chrome_options = Options()

    # --- PERFIL BOT (Aislado) ---
    # Configuración completa para evasión y control.
    chrome_options.add_argument(f"user-data-dir={profile_dir}")
    chrome_options.add_argument("--profile-directory=Default")
    
    # Anti-bot
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")

    if HEADLESS_MODE:
         chrome_options.add_argument("--headless=new")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"❌ Error al iniciar Chrome: {e}")
        print("💡 POSIBLE CAUSA: El directorio de perfil está en uso.")
        print("   SOLUCIÓN: Asegúrese de cerrar todas las instancias de Google Chrome que utilicen este perfil.")
        raise e
