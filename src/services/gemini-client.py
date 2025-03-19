import google.generativeai as genai
from src.config.settings import get_settings

def configure_gemini():
    settings = get_settings()
    genai.configure(api_key=settings.gemini_api_key)

def generate_character(data: dict, is_nsfw: bool) -> str:
    configure_gemini()  # Добавляем инициализацию API
    
    prompt = f"""
    Создай детальное описание персонажа:
    Имя: {data.get('name', '')}
    Возраст: {data.get('age', '')}
    Стиль общения: {data.get('communication_style', '')}
    Поведение: {data.get('behavior', '')}
    Детали: {data.get('details', '')}
    {"🔞 Режим 18+ активирован" if is_nsfw else ""}
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
