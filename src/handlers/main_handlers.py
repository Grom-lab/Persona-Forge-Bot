from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update
from src.services.gemini_client import generate_character
from src.config.settings import get_settings

# Обработчик команды /start
async def start(update: Update, context):
    await update.message.reply_text(
        "🔮 Добро пожаловать в PersonaForge!\n"
        "Используйте /create чтобы начать создание персонажа"
    )

start_handler = CommandHandler('start', start)

# Обработчик тумблера 18+
async def toggle_nsfw(update: Update, context):
    user_data = context.user_data
    user_data['nsfw'] = not user_data.get('nsfw', False)
    status = "✅ ВКЛЮЧЕН" if user_data['nsfw'] else "🚫 ВЫКЛЮЧЕН"
    await update.message.reply_text(f"18+ режим: {status}")

toggle_nsfw_handler = CommandHandler('toggle_nsfw', toggle_nsfw)
