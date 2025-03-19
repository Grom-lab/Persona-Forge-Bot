from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🔮 Добро пожаловать в PersonaForge!\n"
        "Используйте /create чтобы начать создание персонажа"
    )

start_handler = CommandHandler('start', start)

async def toggle_nsfw(update: Update, context: CallbackContext):
    user_data = context.user_data
    user_data['nsfw'] = not user_data.get('nsfw', False)
    status = "✅ ВКЛЮЧЕН" if user_data['nsfw'] else "🚫 ВЫКЛЮЧЕН"
    await update.message.reply_text(f"18+ режим: {status}")

toggle_nsfw_handler = CommandHandler('toggle_nsfw', toggle_nsfw)
