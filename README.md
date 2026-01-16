# 🤖 Linkedini Bot

Bot automatizado para búsqueda de empleo en LinkedIn, diseñado para mantener una sesión persistente y notificar vía Telegram.

## 📋 Características
- **Sesión Persistente**: Evita tener que iniciar sesión cada vez.
- **Notificaciones Telegram**: Envía alertas de estado y acciones requeridas.


## ⚙️ Configuración de Telegram (Obligatorio)

Para que el bot te envíe notificaciones, necesitas crear tu propio bot de Telegram.

1. **Crear el Bot**:
   - Abre Telegram y busca a **@BotFather**.
   - Envía el comando `/newbot`.
   - Sigue las instrucciones: ponle un nombre (ej. "Mi LinkedIn Bot") y un nombre de usuario (debe terminar en `bot`, ej. `mi_linkedin_personal_bot`).
   - BotFather te dará un **HTTP API Token**. Copia este token.

2. **Obtener tu Chat ID**:
   - Busca a **@userinfobot** en Telegram (o cualquiera similar).
   - Inícialo y te dará tu `Id`. Copia este número.

3. **Configurar en el proyecto**:
   - Renombra el archivo `.env.example` a `.env`.
   - Abre `.env` y pega tus credenciales:
     ```env
     TELEGRAM_BOT_TOKEN=tu_token_aqui
     TELEGRAM_CHAT_ID=tu_id_aqui
     ```

## 🚀 Instalación y Ejecución

### 🪟 Windows

1. **Instalar Python**: Asegúrate de tener Python instalado (márcalo para agregar al PATH).
2. **Abrir Terminal**: Abre PowerShell o CMD en la carpeta del proyecto.
3. **Instalar dependencias**:
   ```powershell
   pip install -r requirements.txt
   ```
4. **Ejecutar**:
   - Doble clic en `run_bot.bat`
   - O desde la terminal: `python main.py`

### 🐧 Linux

1. **Instalar Python y Pip**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
2. **Entorno Virtual (Recomendado)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar**:
   ```bash
   python3 main.py
   ```

### 📱 Termux (Android)

1. **Actualizar paquetes e instalar dependencias del sistema**:
   ```bash
   pkg update && pkg upgrade
   pkg install python clang make libjpeg-turbo freetype chromium
   ```
2. **Instalar dependencias del proyecto**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configuración**:
   - Asegúrate de editar el archivo `.env` (puedes usar `nano .env`).
   - Se recomienda configurar `HEADLESS_MODE=True` en el archivo `.env` si no tienes un entorno gráfico X11 configurado.
4. **Ejecutar**:
   ```bash
   python main.py
   ```

## 🛠️ Tecnologías

Este proyecto está construido con un stack robusto y simple:

- **Python 3.x**: Lenguaje principal.
- **Selenium**: Para la automatización del navegador y scraping.
- **Telegram API**: Para el envío de notificaciones y control remoto.
- **Requests**: Para la comunicación HTTP.
- **Python-Dotenv**: Para gestión segura de variables de entorno.

## 🎮 Comandos de Telegram

Puedes controlar los filtros y búsquedas del bot directamente desde el chat de Telegram, sin necesidad de reiniciar el programa.

| Acción | Comando Principal | Alias (Más cortos) | Ejemplo |
|:---|:---|:---|:---|
| **Agregar Negativa** 🚫 | `/addneg <palabra>` | `/menos`, `/an` | `/menos wordpress` |
| **Eliminar Negativa** 🗑️ | `/delneg <palabra>` | `/sacarmenos`, `/dn` | `/dn php` |
| **Agregar Positiva** ✅ | `/addpos <palabra>` | `/mas`, `/ap` | `/mas rust` |
| **Eliminar Positiva** 🗑️ | `/delpos <palabra>` | `/sacarmas`, `/dp` | `/dp react` |
| **Ver Negativas** 📜 | `/listneg` | `/vermenos`, `/ln` | `/ln` |
| **Ver Positivas** 📜 | `/listpos` | `/vermas`, `/lp` | `/lp` |
| **Ayuda / Comandos** ℹ️ | `/comandos` | `/help`, `/ayuda` | `/ayuda` |
| **Archivar Oferta** 🗃️ | `ya lo vi` | `listo`, `paso`, `visto` | *(Responder al mensaje del bot)* |

## 📂 Estructura del Proyecto

```
linkedini/
├── main.py            # Punto de entrada. Controla el ciclo de vida y los descansos.
├── run_bot.bat        # Script de inicio rápido para Windows.
├── requirements.txt   # Lista de dependencias.
├── .env               # (Crear manualmente) Tus claves y configuraciones privadas.
├── keywords.json      # (Auto-generado) Base de datos de palabras clave (se crea al iniciar).
├── profile/           # (Auto-generado) Carpeta donde se guardan tus cookies de LinkedIn.
├── src/
│   ├── driver.py      # Configuración del navegador Chrome (Sessiones, Anti-bot).
│   ├── linkedin.py    # Lógica de scraping y navegación en LinkedIn.
│   ├── listener.py    # Escucha comandos de Telegram ("ya lo vi", "/menos", etc).
│   ├── history.py     # Gestiona la base de datos de trabajos vistos.
│   ├── keywords_manager.py # Gestiona la persistencia de palabras clave (JSON).
│   ├── notifications.py # Envío de mensajes a Telegram.
│   └── config.py      # Constantes, URLs de búsqueda y Keywords.
└── ...
```

## 🧠 Archivos de Datos (Memoria)

El bot utiliza archivos JSON locales para mantener su "estado":

1.  **`seen_jobs.json`**:
    -   **Función**: Evita duplicados.
    -   Guarda las URLs de todas las ofertas que ya te ha enviado o que has marcado como "vistas".
    -   Se limpia automáticamente cada 30 días.

2.  **`last_update.json`**:
    -   **Función**: Control de mensajería.
    -   Guarda el ID del último mensaje de Telegram procesado para no releer comandos antiguos.

3.  **`keywords.json`**:
    -   **Función**: Configuración dinámica.
    -   Guarda tus listas de palabras positivas y negativas para que no se pierdan al reiniciar el bot.