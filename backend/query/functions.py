from .prompt import create_prompt
import openai
from settings import open_ai_api_key
def query_chatgpt(dish_name: str):

    prompt = create_prompt(dish_name)

    # aca va la logica de conexion con chatgpt

    openai.api_key = open_ai_api_key
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "user", "content": prompt}])

    return parse_response(response)

def parse_response(response: str):

    # aca formateamos la respuesta

    return response

