import requests
import os

from grog import Groq

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
    
    if __name__ == "__main__":
        groq_run = GroqRunTime()

        system_prompt = '''
        buatlah response yang positif dan akurat.
        buatlah response dalam bahasa indonesia.
        tentukan apakah input dari user memiliki sentiment negatif atau positif.
        apabila positif buatlah response **1**, dan negatif **0**.

        berikut ini contoh yang dapat kamu ikuti:

        Sentence : Hari ini hujan dan menyebalkan.
        Sentiment : **0**.

        Sentence: Hari ini saya senang karena piknik dengan keluarga.
        Sentiment : **1**.

        ini akhir dari contoh.

        buatlah response seperti format dibawah ini:
        Sentence: [disini tempat user memasukkan input sentence].
        Sentiment: [disini kamu menentukan sentimen yang di input oleh user apakah negatif **0** atau positif **1**].
        '''

        user_prompt = '''
            tentukan sentiment dari input user dibawah ini.
            ikuti instruksi yang diberikan oleh sistem.

            Sentence: Hari ini saya senang sekali karena makan makanan enak.
            Sentiment:
        '''

        response = groq_run.generate_response(system_prompt, user_prompt)

        print(response.choices[0].message.content)