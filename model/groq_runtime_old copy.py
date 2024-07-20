import requests
import os

from groq import Groq

#prepare the apiKey
with open('api_key.txt', 'r') as txt_r:
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
            temperature = 0.3
            # repetition_penalty = 0.8,
        )
        return responses
    
    if __name__ == "__main__":
        groq_run = GroqRunTime()

        system_prompt = '''
        saya ingin kamu menyimpulkan input user secara akurat.
        buatlah kesimpulan dalam bahasa indonesia
        pastikan kesimpulan yang kamu buat sesuai dengan konten yang diberikan oleh user.

        ikutilah format dibawah ini saat membuat response :
        Sentence: [disini tempat user memasukkan input sentence].
        Summary: [disini kamu menuliskan kesimpulan dari input yang diberikan oleh user].
        '''

        user_prompt = '''
        buatlah kesimpulan dari user input:
        
        Sentence: Saya ingin membeli sebuah mobil, tetapi saya bingung memilih mobil yang cocok untuk saya.
        Summary: 
        '''

        response = groq_run.generate_response(system_prompt, user_prompt)

        print(response.choices[0].message.content)