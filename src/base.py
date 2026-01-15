from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from src.notifications import send_telegram_message
from src.history import history

class BaseBot(ABC):
    """
    Clase madre para todos los bots de búsqueda de empleo.
    Provee métodos comunes de Selenium y lógica básica.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # Espera máxima de 10 segundos para encontrar elementos

    @abstractmethod
    def login(self):
        """Implementación de la lógica de inicio de sesión."""
        pass

    @abstractmethod
    def search(self, keyword):
        """Implementación de la lógica de búsqueda de empleos por palabra clave."""
        pass

    # --- Métodos de Ayuda (Utilidad general para bots) ---
    
    def random_sleep(self, min_seconds=2, max_seconds=5):
        """
        Espera un tiempo aleatorio.
        Simulación de comportamiento humano para evitar detección automatizada.
        """
        time.sleep(random.uniform(min_seconds, max_seconds))

    def safe_click(self, by, value):
        """
        Intento de clic en elemento de forma segura, esperando su aparición.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            return True
        except Exception as e:
            print(f"   ⚠️ No se pudo hacer clic en {value}: {e}")
            return False

    def type_text(self, by, value, text):
        """Escritura de texto en un campo, con limpieza previa."""
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            element.clear()
            element.send_keys(text)
            return True
        except Exception:
            print(f"   ⚠️ No se pudo escribir en {value}")
            return False

    def validate_job_title(self, job_title, search_keywords, negative_keywords):
        """
        Analiza si un título de trabajo es relevante según las palabras clave configuradas.
        """
        import re
        
        normalized_title = job_title.lower()
        
        def contains_exact_word(search_term, content):
            escaped_term = re.escape(search_term)
            if not search_term.isalnum(): 
                pattern = r'(?<!\w)' + escaped_term + r'(?!\w)'
                return re.search(pattern, content) is not None
            try:
                pattern = r'\b' + escaped_term + r'\b'
                return re.search(pattern, content) is not None
            except:
                return search_term in content

        for negative_word in negative_keywords:
            if contains_exact_word(negative_word, normalized_title):
                return None 

        for meaningful_keyword in search_keywords:
            if contains_exact_word(meaningful_keyword, normalized_title):
                return meaningful_keyword
                
        return None

    def notify(self, message):
        """
        Envía una notificación al usuario (Telegram).
        """
        print(f"   📢 Notificación: Mensaje enviado")
        try:
            send_telegram_message(message)
        except Exception as e:
            print(f"   ⚠️ Error enviando Telegram: {e}")

    def check_and_track(self, url):
        """
        Verifica si la URL ya fue vista.
        """
        if not url: return True
        
        if history.is_seen(url):
            return False 
        else:
            return True
