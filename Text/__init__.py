def translate_text(strings: dict, key: str, language: str, *args) -> str:
    language = "en" if language not in ["ru", "en"] else language
    return strings[key][language](*args)


def translate_button(strings: dict, key: str, language: str) -> str:
    language = "en" if language not in ["ru", "en"] else language
    return strings[key][language]