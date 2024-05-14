class Resumentexto:

    model_openai = "gpt-3.5-turbo"

    def __init__(self, api_key):
        self.api_key = api_key
    
    def resumen(self,idioma,texto):
        from openai import OpenAI
        client = OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model = self.model_openai,
            messages=[
            {"role": "system", "content":"Eres un asistente que puede leer un texto y resumirlo. Su resumen tendrá 10 oraciones o menos y será en el siguiente idioma: "+idioma},
            {"role": "user", "content": "El texto que quiero resumir es el siguiente: \n"+texto},
            ],
        )
    
        respuesta = response.choices[0].message.content
        client.close()
        return respuesta