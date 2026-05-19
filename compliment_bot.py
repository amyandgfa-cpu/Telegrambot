from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

BOT_TOKEN = "8680845425:AAFnMps_eI9AN-8UyHaK1LDnhOfzXmhFGSg"

COMPLIMENTS = [
    "Ты сегодня выглядишь просто потрясающе ✨",
    "Знаешь, таких людей как ты — единицы 💛",
    "Твоя улыбка способна улучшить день любому 😊",
    "Ты умнее, чем думаешь о себе 🧠",
    "Мир определённо стал лучше, когда ты в нём появился(ась) 🌍",
    "Ты вдохновляешь людей, даже не подозревая об этом 🌟",
    "Твоя доброта — настоящая суперсила 💪",
    "Рядом с тобой всем становится теплее ☀️",
    "Ты справишься со всем, за что берёшься 🚀",
    "Кто-то сегодня думает о тебе и улыбается 💭",
    "Ты заслуживаешь всего самого лучшего 🎁",
    "Твоя энергия заряжает всех вокруг ⚡",
    "Ты особенный(ая) — и это не просто слова 🦋",
    "С тобой рядом хочется быть лучше 🌺",
    "Ты делаешь этот мир красивее просто своим присутствием 🌸",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 🌸 Я буду говорить тебе приятное.\n"
        "Напиши что-нибудь — и получишь порцию тепла 💛"
    )

async def send_compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    compliment = random.choice(COMPLIMENTS)
    await update.message.reply_text(compliment)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_compliment))
    print("Бот запущен!")
    app.run_polling()
