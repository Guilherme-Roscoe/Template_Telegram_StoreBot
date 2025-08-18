from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 Substitua pelo token do seu bot
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Menu principal
def get_main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Recarregar", callback_data='menu_recarregar')],
        [InlineKeyboardButton("Comprar", callback_data='menu_comprar')],
    ])

# Submenu de recarga
def get_recarregar_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("R$10", callback_data='recarregar_10')],
        [InlineKeyboardButton("R$20", callback_data='recarregar_20')],
        [InlineKeyboardButton("🔙 Voltar", callback_data='voltar')],
    ])

# Submenu de compras
def get_comprar_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Produto A", callback_data='comprar_a')],
        [InlineKeyboardButton("Produto B", callback_data='comprar_b')],
        [InlineKeyboardButton("🔙 Voltar", callback_data='voltar')],
    ])

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"👋 Olá, {user.first_name}! Bem-vindo ao nosso bot.\nEscolha uma das opções abaixo:"
    await update.message.reply_text(welcome_text, reply_markup=get_main_menu())

# Manipula todos os botões
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # Menus principais
    if data == 'menu_recarregar':
        await query.edit_message_text("💰 Escolha um valor para recarregar:", reply_markup=get_recarregar_menu())
    elif data == 'menu_comprar':
        await query.edit_message_text("🛍️ Escolha um produto:", reply_markup=get_comprar_menu())

    # Subopções de recarga
    elif data == 'recarregar_10':
        await query.edit_message_text("✅ Você escolheu recarregar R$10.")
    elif data == 'recarregar_20':
        await query.edit_message_text("✅ Você escolheu recarregar R$20.")

    # Subopções de compra
    elif data == 'comprar_a':
        await query.edit_message_text("🛒 Você escolheu: Produto A.")
    elif data == 'comprar_b':
        await query.edit_message_text("🛒 Você escolheu: Produto B.")

    # Voltar para o menu principal
    elif data == 'voltar':
        await query.edit_message_text("⬅️ Menu principal:", reply_markup=get_main_menu())

# Função principal
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
