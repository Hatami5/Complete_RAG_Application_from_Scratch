#Loader.py
from langchain_community.document_loaders import pypdf,pymupdf, textloader
from pathlib import Path
from typing import List, Any
def loader(data: str)->list[Any]:
    data =Path(data).resolve()
    data_load =[]
    pdf =data.glob('**/*.pdf')
    
    for i in pdf():
        try:
            pdf_file = PyPDFLoader(str(i))
            pdf_file =pdf_file.load()
            data_load.extend(pdf_file)
        except Exception as e:
            print(f"[Error] while loading fil:{i}: {e}")
### Text loader......
    pdf =data.glob('**/*.text')
    
    for i in pdf():
        try:
            pdf_file =textloader(str(i))
            pdf_file =pdf_file.load()
            data_load.extend(pdf_file)
        except Exception as e:
            raise ValueError("Error while loading files")
    return data_load
   


    

    





