import requests
import os
import json
import sys

from model.groq_runtime_v03 import GroqRunTime
from utils.prompt import *

#prepare the apiKey
with open('api_key.txt', 'r') as txt_r:
    os.environ["GROQ_API_KEY"] = txt_r.readlines()[0]

class ArrangeDatabase(GroqRunTime):
    def __init__(self):
        super(ArrangeDatabase, self).__init__(api_key = os.environ.get("GROQ_API_KEY"))

    def load_data(self):
        with open('datasets/pp_nomor_30_tahun_2021.pdf.json', 'r') as json_r:
            datasets = json.load(json_r)
        # print(data)
        for i_data, data in enumerate(datasets):
            user_prompt = USER_PROMPT_CLEAN_DATA.format(input_user = data['content'])

            response = self.generate_response(SYSTEM_PROMPT_CLEAN_DATA, user_prompt)

            print(data['content'])
            print('-'*50)
            print(response.choices[0].message.content)
            sys.exit()