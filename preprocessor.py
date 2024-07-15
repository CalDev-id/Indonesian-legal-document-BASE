import os 
import json
from pypdf import PdfReader
from tqdm import tqdm

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import JSONLoader

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# from langchain.embeddings import SentenceTransformerEmbeddings

class Preprocessor():
    def __init__(self) -> None:
        self.raw_data_dir = "raw_data"

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1",
            model_kwargs={"device": "cpu"},
            encode_kwargs = {"normalize_embeddings": False}
        )
        # self.embeddings = SentenceTransformerEmbeddings(
        #     model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1",
        #     model_kwargs={"device": "cpu"},
        #     encode_kwargs = {"normalize_embeddings": False}
        # )

        self.database_save_dir = "datasets/database_{db_name}"
    def load_data(self):
        list_file_raw = os.listdir(self.raw_data_dir)
        for fl_raw in list_file_raw:
            fl_dir = f"{self.raw_data_dir}/{fl_raw}"

            #load pdf file
            pdf_content = PdfReader(fl_dir)
            n_pages = len(pdf_content.pages)

            datasets = []

            n_pages = len(pdf_content.pages)
            for n_p in range(n_pages):
                page_content = pdf_content.pages[n_p]
                page_content = page_content.extract_text()

                if page_content != "":
                    datasets.append({
                        "page": n_p,
                        "content": page_content
                    })


            with open(f"datasets/{fl_raw.lower().replace('-', '_')}.json", "w") as json_w:
                json.dump(datasets, json_w, indent = 4)
            
    def load_data_json_lib(self, source_dir):
        loader = JSONLoader(
            file_path = source_dir,
            jq_schema=".[] | {contents: .content}",
            text_content =  False,
            json_lines = False,
            content_key = "contents"
        )
        data = loader.load()
        text_splitter = CharacterTextSplitter(
            chunk_size = 1000,
            overlap = 0
        )
        data = text_splitter.split_documents(data)
        return data

    def create_faiss_db(self, source, db_name):
        data = self.load_data_json_lib(source)

        db = FAISS.from_documents(data, self.embeddings)
        db.save_local(self.database_save_dir.format(
            db_name = db_name
        ))

    def search_db(self, query, db_name):
        database_provider = FAISS.load_local(
            self.database_save_dir.format(db_name = db_name),
            self.embeddings,
            allow_dangerous_deserialization = True
        )

        search_results = database_provider.similarity_search(query, k = 5, fetch_k = 10)
        print(search_results[0])

if __name__ == "__main__":
    preprocessor = Preprocessor()
    # preprocessor.load_data()

    preprocessor.create_faiss_db("datasets/pp_no_76_thn_2020_ttg_tarif_pnbp_polri.pdf.json", db_name="pp_no_76" )

    # Preprocessor.search_db(query = "apa jenis penerimaan negara bukan pajak", db_name = "pp_no_76")
    preprocessor.search_db(query = "apa pengelompokan wilayah pendidikan", db_name = "pp_no_76")
