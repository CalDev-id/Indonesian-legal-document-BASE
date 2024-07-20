import requests
import os
import json

from model.groq_runtime_v03 import GroqRunTime

#prepare the apiKey
with open('api_key.txt', 'r') as txt_r:
    os.environ["GROQ_API_KEY"] = txt_r.readlines()[0]

class ArrangeDatabase(GroqRunTime):
    def __init__(self):
        super(ArrangeDatabase, self).__init__(api_key = os.environ.get("GROQ_API_KEY"))

    def load_data(self):
        with open('datasets/pp_nomor_30_tahun_2021.pdf.json', 'r') as json_r:
            data = json.load(json_r)
        print(data)
        return data