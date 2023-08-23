from .prompt import create_prompt
def query_chatgpt(dish_name: str):

    prompt = create_prompt(dish_name)

    # aca va la logica de conexion con chatgpt

    return parse_response(prompt)

def parse_response(response: str):

    # aca formateamos la respuesta

    return response