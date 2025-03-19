import os
from dotenv import load_dotenv
from telegram.ext import Application
from src.handlers.main_handlers import start_handler, toggle_nsfw_handler
from src.handlers.form_handlers import form_conversation_handler

load_dotenv()

async def post_init(app: Application):
    await app.bot.set_my_commands([
        ("start", "Создать нового персонажа"),
        ("toggle_nsfw", "Включить/выключить 18+")
    ])

def main():
    app = Application.builder()\
        .token(os.getenv("TELEGRAM_BOT_TOKEN"))\
        .post_init(post_init)\
        .build()
    
    app.add_handler(start_handler)
    app.add_handler(form_conversation_handler)
    app.add_handler(toggle_nsfw_handler)
    
    app.run_polling()

if __name__ == "__main__":
    main()
