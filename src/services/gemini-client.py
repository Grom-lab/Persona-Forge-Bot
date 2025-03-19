import google.generativeai as genai
from src.config.settings import get_settings

def configure_gemini():
    settings = get_settings()
    genai.configure(api_key=settings.gemini_api_key)

def generate_character(data: dict, is_nsfw: bool) -> str:
    prompt = f"""
    Создай детальное описание персонажа на основе данных:
    Имя: {data['name']}
    Возраст: {data['age']}
    Стиль общения: {data['communication_style']}
    Особенности поведения: {data['behavior']}
    Дополнительные детали: {data['details']}
    {"Режим 18+ включен" if is_nsfw else ""}
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
