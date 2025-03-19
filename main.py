import os
from dotenv import load_dotenv
from telegram.ext import Application
from src.handlers import main_handlers, form_handlers

load_dotenv()

async def post_init(app: Application):
    await app.bot.set_my_commands([
        ("start", "Создать нового персонажа"),
        ("toggle_nsfw", "Включить/выключить 18+")
    ])

def main():
    app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).post_init(post_init).build()
    
    # Регистрация обработчиков
    app.add_handler(main_handlers.start_handler)
    app.add_handler(form_handlers.form_conversation_handler)
    app.add_handler(main_handlers.toggle_nsfw_handler)
    
    app.run_polling()

if __name__ == "__main__":
    main()
