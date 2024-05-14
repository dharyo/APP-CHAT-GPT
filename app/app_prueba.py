import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content":"Eres un experto en cocina y en nutricion"},
        {"role": "user", "content": "Dame una receta para preparar unos chicharrones de cedo crujientes y saludables"},
    ],
)

respuestas = response.choices[0].message.content

print(respuestas)
client.close()
