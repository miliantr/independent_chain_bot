from aiogram import Router
from aiogram.fsm.state import StatesGroup, State


class ModulesManager:
    def __init__(self, name: str):
        self.name = name
        self.router = Router()
        self.modules = dict()

    def connect(self, path: str, name: str) -> None:
        module = __import__(f"{path}.{name}", fromlist=[""])
        self.modules[name] = module
        return None

    def disconnect(self, name: str) -> None:
        del self.modules[name]
        return None


class MainModuleStates(StatesGroup):
    mining = State()
    upgrades = State()
    wallet = State()
    codes = State()
    geckoshi = State()
    slots = State()


class AdminModuleStates(StatesGroup):
    panel = State()
    messages = State()
    mail = State()
    mailing = State()
    database = State()
    codes = State()
    generate_codes = State()
    get_codes = State()
    statistics = State()
    get_values = State()
    change_values = State()
