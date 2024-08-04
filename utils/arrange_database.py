import requests
import os
import json
import sys
from pypdf import PdfReader

from model.groq_runtime_v03 import GroqRunTime
from utils.prompt import *

from tqdm import tqdm

#prepare the apiKey
with open('api_key.txt', 'r') as txt_r:
    os.environ["GROQ_API_KEY"] = txt_r.readlines()[0]

class ArrangeDatabase(GroqRunTime):
    def __init__(self):
        super(ArrangeDatabase, self).__init__(api_key = os.environ.get("GROQ_API_KEY"))
        self.raw_data_dir = "datasets/raw_data"

    def data_cleaning(self):
        #stanza data cleaning
        pass

    def extract_page(self, page_contents, n_p):
        page_contents = page_contents.split("\n")

        if n_p == 1:
            flag_content = False
        else:
            flag_content = True

        data = {
            "bab": 1,
            "bab_penjelasan": "ketentuan_umum",
            "pasal": 1,
            "item_no": 1,
            "item": "sentence"
        }

        for pg_conts in page_contents:
            #print(pg_conts)
            if n_p == 1 and "bab i" in pg_conts.lower():
                flag_content = True
                print(pg_conts)

                
    
    def load_data(self):
        list_file_raw = os.listdir(self.raw_data_dir)
        for fl_raw in tqdm(list_file_raw, desc="pdf to json"):
            fl_dir = f"{self.raw_data_dir}/{fl_raw}"

            #load pdf file
            pdf_content = PdfReader(fl_dir)
            n_pages = len(pdf_content.pages)

            datasets = []

            n_pages = len(pdf_content.pages)
            for n_p in range(n_pages):
                page_content = pdf_content.pages[n_p]
                page_content = page_content.extract_text()

                extracted_page = self.extract_page(page_content)


    def clean_data(self):
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