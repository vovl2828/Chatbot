from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8457232343:AAEfoiLRidEmOFDweVFP5FqVJLEcJP9wkaw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Привіт! Я бот магазину WinSoftMarket.\n"
        "Тут ти можеш отримати цифровий промокод після оплати.\n\n"
        "📋 Доступні команди:\n"
        "/getcode — отримати промокод\n"
        "/info — про магазин\n"
        "/help — інструкція"
    )

@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.answer(
        "🛍️ WinSoftMarket — це цифровий магазин ліцензійних ключів та промокодів.\n"
        "🎁 Пропонуємо коди для YouTV, Sweet.TV, Windows, Office тощо."
    )

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(
        "ℹ️ Щоб отримати промокод:\n"
        "1️⃣ Оплати товар на сайті WinSoftMarket.\n"
        "2️⃣ Відправ команду /getcode.\n"
        "3️⃣ Отримай свій промокод автоматично 💥"
    )

@dp.message_handler(commands=['getcode'])
async def get_code(message: types.Message):
    try:
        with open("codes.txt", "r") as f:
            codes = f.readlines()

        if not codes:
            await message.answer("❌ Промокоди закінчились.")
            return

        code = codes[0].strip()
        await message.answer(f"✅ Ваш промокод: {code}")

        with open("codes.txt", "w") as f:
            f.writelines(codes[1:])
    except FileNotFoundError:
        await message.answer("⚠️ Файл codes.txt не знайдено. Додайте його в папку.")
    except Exception as e:
        await message.answer(f"⚠️ Помилка: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)