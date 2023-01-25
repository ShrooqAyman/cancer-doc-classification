import string 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize

class PreProcessing:
    def __init__(self):
        pass

    def transform(self, data):
        #removing special character
        def remove_special_char(list):
            y=[]
            for string in list:
                if string.isalnum():
                    y.append(string)
            return y
        
        #remove stopwords like is am are and punctuations
        def useful_words(list):
            y=[]
            for text in list:
                if text not in stopwords.words('english') and text not in string.punctuation:
                        y.append(text)
            return y
        
        #convert into root words
        ps = PorterStemmer()
        def stemming(list):
            y=[]
            for text in list:
                y.append(ps.stem(text))
            return y
        
        
        data = data.lower()
        data = word_tokenize(data)
        data = remove_special_char(data)
        data = useful_words(data)
        data = stemming(data)
        data2 = " ".join(data)
        return data2