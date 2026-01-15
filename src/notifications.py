import requests
from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(message):
    """
    Envía un mensaje a Telegram mediante solicitud HTTP POST.
    Retorna True si el envío fue exitoso (Status 200).
    """
    
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("   ⚠️ Configuración de Telegram incompleta (Falta TOKEN o CHAT_ID). Mensaje omitido.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,             
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code == 200:
            return True
        else:
            print(f"   ❌ Error en la API de Telegram: {response.text}")
            return False
            
    except Exception as e:
        print(f"   ❌ Excepción al enviar a Telegram: {e}")
        return False
