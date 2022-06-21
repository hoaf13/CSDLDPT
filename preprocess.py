from underthesea import word_tokenize, sent_tokenize
import string
from config import *
class DataPreprocessor:
    
    def __init__():
        pass 


    @staticmethod
    def remove_punctuation(text: str) -> str:
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text        

    @staticmethod
    def segment_sentence(document:str) -> list:
        paragraphs = document.split("\n")
        sentences = []
        for paragraph in paragraphs:
            sentences.extend(sent_tokenize(paragraph))
        return sentences
    
    @staticmethod
    def segment_word(text:str) -> list:
        words = word_tokenize(text,)
        return words

    @staticmethod
    def to_lower(text:str) -> str:
        return text.lower()

    @staticmethod
    def remove_stopwords(words: list) -> list: 
        def load(stopword_path):
            f = open(stopword_path,'r')
            lines = f.readlines()
            f.close()
            stopwords = [line[:-1] for line in lines]
            return stopwords

        stopwords = load(STOPWORD_PATH)
        res = [x for x in words if x not in stopwords]
        return res
    
    @staticmethod
    def get_list_words(document: str) -> list:
        pass