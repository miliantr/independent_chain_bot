from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.button_constructor import button


def menu_kb(user_id: int, language: str) -> InlineKeyboardMarkup:
    strings: dict[str, dict] = {
        "invitation": {
            "ru": "\nПрисоединяйся к Independent Chain.\nНам важен каждый ⚡️",
            "en": "\nJoin the Independent Chain.\nEveryone is important to us ⚡️"
        }
    }
    referal_link: str = f"{strings["invitation"][language]}\nhttps://t.me/inch_coin_bot?start={user_id}"
    buttons: dict[str, list] = {
        "ru": [button(signature="👤 Профиль", callback="profile"),
               button(signature="💳 Кошелёк", callback="wallet"),
               button(signature="📚 Информация", callback="information"),
               button(signature="🛟 Поддержка", callback="support"),
               button(signature="🎉 События", callback="events"),
               InlineKeyboardButton(text="Пригласить друга", switch_inline_query=referal_link)],
        "en": [button(signature="👤 Profile", callback="profile"),
               button(signature="💳 Wallet", callback="wallet"),
               button(signature="📚 Information", callback="information"),
               button(signature="🛟 Support", callback="support"),
               button(signature="🎉 Events", callback="events"),
               InlineKeyboardButton(text="Invite friend", switch_inline_query=referal_link)]
    }
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.row(buttons[language][0], buttons[language][1])
    builder.row(buttons[language][2], buttons[language][3])
    builder.row(buttons[language][4])
    builder.row(buttons[language][5])
    return builder.as_markup()