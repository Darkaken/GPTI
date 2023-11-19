from prompt import create_prompt
import openai
from config import get_settings

def query_chatgpt(dish_name: str):

    prompt = create_prompt(dish_name)

    # aca va la logica de conexion con chatgpt

    openai.api_key = get_settings().open_ai_key
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "user", "content": prompt}])

    return parse_response(response)

def parse_response(response: str):

    # aca formateamos la respuesta

    return response

