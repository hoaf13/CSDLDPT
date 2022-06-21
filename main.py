from preprocess import DataPreprocessor
from load_dataset import DataLoader
from config import * 
import json 

if __name__ == "__main__":
    documents = DataLoader.load(dataset_path=DATASET_PATH)
    dataset = {}
    for ele in documents:
        filename = ele[0]
        document = ele[1]
        dataset[filename] = {
            "document": document,
            "sentences": [],
            "words": []
        }  
    
    for idx,filename in enumerate(dataset):
        print(f"{idx+1}/{len(dataset)}")
        document = dataset[filename]["document"]
        sentences = DataPreprocessor.segment_sentence(document)
        sentences = [DataPreprocessor.to_lower(sentence) for sentence in sentences]
        sentences = [DataPreprocessor.remove_punctuation(sentence) for sentence in sentences]
        document = dataset[filename]["sentences"] = sentences

        word_list = list()
        for sentence in sentences:
            words = DataPreprocessor.segment_word(sentence)
            word_list.extend(words) 
        
        dataset[filename]["words"] = word_list

        

    with open("dataset.json", "w", encoding='utf8') as outfile:
        json.dump(dataset, outfile, ensure_ascii=False)