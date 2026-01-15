import os
import sys
from dotenv import load_dotenv

# Carga del archivo .env desde la raíz del proyecto
load_dotenv()

# Credenciales de Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Configuración del Navegador
# HEADLESS_MODE: Si es True, el navegador no muestra interfaz gráfica (útil para servidores).
# Por defecto es False para facilitar la depuración y el inicio de sesión manual.
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() == "true"

# Intervalo entre rondas de búsqueda completa (en minutos)
# Por defecto: 360 minutos (6 horas)
SEARCH_INTERVAL = int(os.getenv("SEARCH_INTERVAL", 360))

# --- URLs DE BÚSQUEDA ---
# El bot recorrerá cada una de estas URLs secuencialmente.
# INSTRUCCIONES:
# 1. Ve a LinkedIn "Empleos".
# 2. Realiza tu búsqueda con los filtros que desees (Ubicación, Remoto, Fecha de publicación, etc).
# 3. Copia la URL del navegador y pégala aquí.
JOB_SEARCH_URLS = [
    # === Filtros de ultima semana ===
    # Desarrollador ARG
    "https://www.linkedin.com/jobs/search/?currentJobId=4353192033&f_AL=true&f_TPR=r604800&geoId=100446943&keywords=Desarrollador&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD",

    # Desarrollador España (Remoto)
    "https://www.linkedin.com/jobs/search/?currentJobId=4352619718&f_AL=true&f_TPR=r604800&f_WT=2&geoId=105646813&keywords=Desarrollador&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD",

    # Desarrollador Todo el mundo (Remoto)
    "https://www.linkedin.com/jobs/search/?currentJobId=4361667042&f_AL=true&f_TPR=r604800&f_WT=2&geoId=92000000&keywords=Desarrollador&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&sortBy=DD",

    # Programador ARG
    "https://www.linkedin.com/jobs/search/?currentJobId=4353004987&f_AL=true&f_TPR=r604800&geoId=100446943&keywords=Programador&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD",

    # Programador España (Remoto)
    "https://www.linkedin.com/jobs/search/?currentJobId=4353084758&f_AL=true&f_TPR=r604800&f_WT=2&geoId=105646813&keywords=Programador&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD",

    # Programador Todo el mundo (Remoto)
    "https://www.linkedin.com/jobs/search/?currentJobId=4359080675&f_AL=true&f_TPR=r604800&f_WT=2&geoId=92000000&keywords=Programador&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&sortBy=DD"
]

# --- PALABRAS CLAVE DE BÚSQUEDA ---
SEARCH_KEYWORDS = [
    "desarrollo web", 
    "frontend", 
    "programador web", 
    "python",
    "programador",
    "react",
    "javascript",  
    "maquetador web",
    "web developer",
    "front-end",
    "desarrollador",
    "desarrollador web",
    "desarrollador frontend",
    "desarrollador backend",
    "developer",
    "pasantía desarrollador",
    "pasantía programador",
    "pasantia programador",
    "pasantia desarrollador",
    "pasante desarrollador",
    "pasante programador"
]

# --- PALABRAS CLAVE NEGATIVAS ---
# Si el título del trabajo contiene CUALQUIERA de estas palabras, será descartado automáticamente.
# Útil para filtrar por seniority (Senior, Lead), tecnologías que no se manejan (ej. .NET, Java) o roles irrelevantes.
NEGATIVE_KEYWORDS = [
    "senior", 
    "sr", 
    "ssr", 
    "lead", 
    "arquitecto", 
    "+3 años", 
    "+4 años", 
    "+5 años",
    "ingles avanzado", 
    "bilingue",
    ".net",
    "net",
    "cobol",
    "angular",
    "vue",
    "analista de datos",
    "power bi",
    "qa",
    "c#",
    "c++",
    "arduino",
    "PLC",
    "soporte it",
    "wordpress",
    "devops",
    "sysadmin",
    "php",
    "laravel",
    "django",
    "fullstack",
    "full stack",
    "full-stack",
    "sap",
    "sap abap",
    "abap",
    "cloud",
    "aws",
    "azure",
    "google cloud",
    "google-cloud",
    "java",
    "data science",
    "data",
    "ux/ui",
    "ux ui",
    "ux",
    "ui",
    "pruebas",
    "pl",
    "sql",
    "engineer",
    "enginner",
    "enginer",
    "ingeniero",
    "native",
    "lider",
    "líder",
    "next.js",
    "next",
    "business",
    "webflow",
    "salesforce",
    "oracle",
    "ingles",
    "english",
    "wpf",
    "snowflake",
    "shopify",
    "dotnet",
    "blueprism",
    "mobile",
    "ios",
    "android",
    "swift",
    "kotlin",
    "native",
    "flutter",
    "dart",
    "xamarin",
    "móbiles",
    "Base24",
    "Osb",
    "tibco",
    "nest.js",
    "nest",
    "mainframe",
    "mainframes",
    "cobol",
    "inglés",
    "appian",
    "apache",
    "apx",
    "android",
    "ios",
    "swift",
    "kotlin",
    "flutter",
    "dart",
    "brazil",
    "brasil",
    "dynamics 365"
]
