import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TOKEN

API_TOKEN = TOKEN

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def show_initial_button(message: types.Message):
    # Создаем инлайн-кнопку "Показать больше"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")],
    ])
    await message.answer("Нажмите кнопку ниже:", reply_markup=keyboard)

# Обработчик нажатия на инлайн-кнопки
@dp.callback_query()
async def handle_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "show_more":
        # Заменяем кнопку "Показать больше" на кнопки "Опция 1" и "Опция 2"
        new_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
            [InlineKeyboardButton(text="Опция 2", callback_data="option_2")],
        ])
        await callback_query.message.edit_text("Выберите опцию:", reply_markup=new_keyboard)
    elif callback_query.data == "option_1":
        await callback_query.message.answer("Вы выбрали Опция 1")
    elif callback_query.data == "option_2":
        await callback_query.message.answer("Вы выбрали Опция 2")

    # Подтверждаем callback, чтобы убрать индикатор загрузки
    await callback_query.answer()

if __name__ == "__main__":
    dp.run_polling(bot)