from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler

# States
NAME, AGE, COMMUNICATION, BEHAVIOR, DETAILS = range(5)

async def start_form(update, context):
    await update.message.reply_text("Введите имя персонажа:")
    return NAME

async def process_name(update, context):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Введите возраст:")
    return AGE

# ... остальные шаги формы ...

async def finish_form(update, context):
    user_data = context.user_data
    keyboard = [[InlineKeyboardButton("✅ Включить 18+", callback_data='nsfw_on')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Настройки:", reply_markup=markup)
    return ConversationHandler.END
