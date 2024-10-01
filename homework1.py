import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram import F
from config import TOKEN

API_TOKEN = TOKEN

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Определяем кнопки
button_hello = KeyboardButton(text="Привет")
button_goodbye = KeyboardButton(text="Пока")

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_hello, button_goodbye]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@dp.message(F.text == "Привет")
async def message_hello(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"Привет, {user_name}!")

@dp.message(F.text == "Пока")
async def message_goodbye(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"До свидания, {user_name}!")

if __name__ == "__main__":
    dp.run_polling(bot)