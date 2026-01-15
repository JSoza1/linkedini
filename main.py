import time
import sys
from datetime import datetime, timedelta
from src.driver import get_driver
from src.notifications import send_telegram_message
from src.config import SEARCH_INTERVAL
from src.listener import check_telegram_replies

def main():
    print("========================================")
    print("🤖 LINKEDIN BOT - STARTING")
    print("========================================")

    # Notificación de inicio de servicio
    send_telegram_message("🤖 <b>Buscando chamba por LinkedIn</b>")

    while True:
        driver = None
        try:
            print(f"\n🕒 Iniciando ciclo de búsqueda: {datetime.now().strftime('%H:%M:%S')}")
            
            # 1. Start Driver
            try:
                driver = get_driver()
                # ESTRATEGIA 'EAGER': Carga rápida, interactuamos antes de que carguen todos los assets
                driver.page_load_strategy = 'eager'
            except Exception as e:
                print(f"❌ Error crítico al iniciar Chrome: {e}")
                # Si falla el driver, esperamos un poco y reintentamos en vez de salir
                time.sleep(60) 
                continue

            # 2. Lógica Principal
            print("⏳ Iniciando navegación...")
            time.sleep(2)
            
            # --- Módulo de Automatización de LinkedIn ---
            from src.linkedin import LinkedInBot
            
            # Instanciamos el bot con el driver ya configurado
            bot = LinkedInBot(driver)
            
            # 'Login' (en realidad solo verificado de sesión persistente)
            bot.login()
            
            # Ejecutamos la búsqueda maestra
            bot.search()
            
            print(f"✅ Ciclo terminado.")
            send_telegram_message(f"✅ <b>Ciclo finalizado.</b>\nDescansando {SEARCH_INTERVAL} minutos...")

        except KeyboardInterrupt:
            print("\n👋 Bot detenido manualmente.")
            if driver: driver.quit()
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error en ejecución principal: {e}")
            send_telegram_message(f"⚠️ <b>Error en el ciclo:</b> {e}")
        finally:
            if driver:
                print("🔒 Cerrando navegador para liberar memoria...")
                try:
                    driver.quit()
                except:
                    pass

        # Espera para el siguiente ciclo con CHEQUEO DE TELEGRAM
        next_run = datetime.now() + timedelta(minutes=SEARCH_INTERVAL)
        print(f"💤 Durmiendo hasta: {next_run.strftime('%H:%M:%S')} ({SEARCH_INTERVAL} min)")
        print(f"   (Revisaré Telegram cada 10 minutos durante la espera)")

        remaining_seconds = SEARCH_INTERVAL * 60
        check_interval = 600  # 10 minutos en segundos

        try:
            while remaining_seconds > 0:
                # Determinar cuánto dormir en este bloque (el menor entre 10 min o lo que falte)
                sleep_time = min(remaining_seconds, check_interval)
                
                # Dormir el bloque
                time.sleep(sleep_time)
                
                # Descontar tiempo
                remaining_seconds -= sleep_time
                
                # ¡DESPERTAR! Chequear mensajes
                if remaining_seconds > 0:
                    print(f"   👀 Despertando para chequear Telegram... (Faltan {int(remaining_seconds/60)} min)")
                    check_telegram_replies()

        except KeyboardInterrupt:
            print("\n👋 Bot detenido durante la espera.")
            sys.exit(0)

            
if __name__ == "__main__":
    main()

