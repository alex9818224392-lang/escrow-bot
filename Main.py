!pip install pyTelegramBotAPI
import telebot, random, string, re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("9178801837:AAEP6HDvfkimUSBUYfw6jeGQxeV66OPJ6u0")
ESCROWERS = ["@nxt_p2p", "@CwazyShyt"]

@bot.message_handler(commands=['deal'])
def deal(msg):
    text = msg.reply_to_message.text if msg.reply_to_message else msg.text
    b = re.search(r'BUYER\s*:\s*(@?\w+)', text, re.I)
    s = re.search(r'SELLER\s*:\s*(@?\w+)', text, re.I)
    a = re.search(r'DEAL AMOUNT\s*:\s*\$?([0-9]+(?:\.[0-9]+)?)', text, re.I)

    if not (b and s and a):
        bot.reply_to(msg, "❌ Format error! Send details then reply /deal")
        return

    tid = "#TID" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    admin = random.choice(ESCROWERS)
    
    card = (
        f"💰 Deal Amount: ${float(a.group(1)):.2f}\n"
        f"📥 Received Amount: ${float(a.group(1)):.2f}\n"
        f"📤 Release/Refund Amount: ${float(a.group(1)):.2f}\n"
        f"🆔 Trade ID: {tid}\n\n"
        f"Continue the Deal\n"
        f"Buyer: {b.group(1)}\n"
        f"Seller: {s.group(1)}\n\n"
        f"🛡 Escrowed By: {admin}"
    )
    
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⚠️ RAISE DISPUTE", url=f"https://t.me/{admin.replace('@','')}"))
    bot.reply_to(msg, card, reply_markup=kb)

print(">>> BOT IS LIVE AND RUNNING! <<<")
bot.infinity_polling()
