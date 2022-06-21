import os 
from config import * 

class DataLoader:    
    def __init__(self):
        pass 

    @staticmethod
    def load(dataset_path):
        documents = []
        filenames = os.listdir(dataset_path)
        filenames = sorted(filenames)
        print(f"Number of records: {len(filenames)}")
        for filename in filenames:
            f = open(dataset_path + filename, 'r')
            document = f.read()
            f.close()
            documents.append((filename,document))
        return documents
            
if __name__ == "__main__":
    documents = DataLoader.load(dataset_path=DATASET_PATH)
    