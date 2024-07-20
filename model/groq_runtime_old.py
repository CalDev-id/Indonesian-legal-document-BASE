import requests
import os

from qrog import Groq

#prepare the apiKey
with open('apiKey.txt', 'r') as txt_r:
    os.environ["GROQ_API_KEY"] = txt_r.readlines()[0]

class GroqRunTime():
    def __init__(self):
        self.client = Groq(
            # this is the default and can be omitted
            api_key=os.environ.get("GROQ_API_KEY"),
        )

    def generate_response(self, system_prompt, user_prompt):
        responses = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            model = "llama3-70b-8192"
        )
        return responses