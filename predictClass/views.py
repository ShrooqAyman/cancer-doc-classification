from django.shortcuts import render
from django.http import JsonResponse
from .preprocessingPipline import PreProcessing

import pandas as pd
import json
import pickle


MODEL_PATH = 'saved_model.sav'
TFIDF_PATH = 'tfidf.sav'

model = pickle.load(open(MODEL_PATH, 'rb'))
tfidf = pickle.load(open(TFIDF_PATH, 'rb'))
preProcessing_pipline = PreProcessing()

def IndexView(request):
    return render(request, 'index.html')

def predicts(request):
   
    if request.POST.get('action') == 'post':
        doc = request.POST['doc']
        processed_doc = preProcessing_pipline.transform(doc)
        processed_doc_series = pd.Series(processed_doc)
        
        doc_vectorized = tfidf.transform(processed_doc_series).toarray()        
        predicted_class = model.predict(doc_vectorized)
       
        lists = predicted_class.tolist()
        json_str = json.dumps(lists[0])
        data = {'predicted_class':json_str}
        return JsonResponse(data, safe=False)

