import json
import os
from datetime import datetime, timedelta

# Definimos constantes para fácil configuración
HISTORY_FILE = "seen_jobs.json" 
DAYS_TO_REMEMBER = 30           

class JobHistory:
    """
    Gestiona la persistencia de ofertas vistas para evitar duplicados.
    """
    
    def __init__(self):
        self.seen_jobs = {}
        self.load()

    def load(self):
        """
        Carga el historial y purga registros más antiguos que DAYS_TO_REMEMBER.
        """
        if not os.path.exists(HISTORY_FILE):
            self.seen_jobs = {}
            return

        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            # Limpieza de registros expirados
            cleaned_data = {}
            limit_date = datetime.now() - timedelta(days=DAYS_TO_REMEMBER)
            
            for url, date_str in data.items():
                try:
                    seen_date = datetime.fromisoformat(date_str)
                    if seen_date > limit_date:
                        cleaned_data[url] = date_str
                except ValueError:
                    continue 
            
            self.seen_jobs = cleaned_data
            self.save() 

        except (json.JSONDecodeError, Exception) as e:
            print(f"⚠️ Error cargando historial: {e}. Se iniciará uno nuevo.")
            self.seen_jobs = {}

    def save(self):
        """Persiste el historial en disco (JSON)."""
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.seen_jobs, f, indent=4)
        except Exception as e:
            print(f"⚠️ No se pudo guardar el historial: {e}")

    def is_seen(self, url):
        """Verifica si una URL ya existe en el registro."""
        # Limpiamos la URL de parámetros de rastreo (LinkedIn pone muchos ?refId=...)
        # para que la comparación sea más efectiva.
        clean_url = url.split("?")[0]
        
        # Chequeo flexible: si la URL limpia o la completa están en el historial.
        return (url in self.seen_jobs) or (clean_url in self.seen_jobs)

    def add_job(self, url):
        """
        Registra una URL con la fecha actual y guarda cambios.
        """
        # Guardamos la URL tal cual, y opcionalmente podríamos guardar la limpia también.
        self.seen_jobs[url] = datetime.now().isoformat()
        
        clean_url = url.split("?")[0]
        if clean_url != url:
             self.seen_jobs[clean_url] = datetime.now().isoformat()
             
        self.save()

# Instancia global para usar en todo el proyecto
history = JobHistory()
