from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 Substitua pelo seu token do BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensagem de boas-vindas
    welcome_text = "👋 Olá! Bem-vindo ao nosso bot.\nEscolha uma das opções abaixo:"

    # Cria os botões
    keyboard = [
        [InlineKeyboardButton("Recarregar", callback_data='recarregar')],
        [InlineKeyboardButton("Comprar", callback_data='comprar')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envia a mensagem com os botões
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Quando um botão é pressionado
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'recarregar':
        await query.edit_message_text("🔄 Você escolheu: Recarregar")
    elif query.data == 'comprar':
        await query.edit_message_text("🛒 Você escolheu: Comprar")

# Função principal
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
