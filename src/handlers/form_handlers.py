from telegram import (
    Update, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    ReplyKeyboardRemove
)
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    CallbackQueryHandler
)

NAME, AGE, COMMUNICATION, BEHAVIOR, DETAILS = range(5)

async def start_form(update: Update, context: CallbackContext):
    await update.message.reply_text("Введите имя персонажа:")
    return NAME

async def process_name(update: Update, context: CallbackContext):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Введите возраст:")
    return AGE

async def process_age(update: Update, context: CallbackContext):
    context.user_data['age'] = update.message.text
    await update.message.reply_text("Опишите стиль общения:")
    return COMMUNICATION

async def process_communication(update: Update, context: CallbackContext):
    context.user_data['communication_style'] = update.message.text
    await update.message.reply_text("Особенности поведения:")
    return BEHAVIOR

async def process_behavior(update: Update, context: CallbackContext):
    context.user_data['behavior'] = update.message.text
    await update.message.reply_text("Дополнительные детали:")
    return DETAILS

async def process_details(update: Update, context: CallbackContext):
    context.user_data['details'] = update.message.text
    keyboard = [
        [InlineKeyboardButton("✅ Включить 18+", callback_data='nsfw_on')],
        [InlineKeyboardButton("🚫 Выключить 18+", callback_data='nsfw_off')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Настройки 18+:", reply_markup=markup)
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Создание отменено", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

form_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('create', start_form)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_name)],
        AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_age)],
        COMMUNICATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_communication)],
        BEHAVIOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_behavior)],
        DETAILS: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_details)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
    )
