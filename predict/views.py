from django.shortcuts import render
import pandas as pd

# Create your views here.
def predict(request):
    return render(request,'predict.html',{'name':'vidhya'})

def prediction(request):
    sepal_length = request.POST['sepal_length']
    sepal_width = request.POST['sepal_width']
    petal_length = request.POST['petal_length']
    petal_width = request.POST['petal_width']
        # Unpickle model
    model = pd.read_pickle(r"new_model.pickle")
        # Make prediction
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    classification = result[0]

    return render(request,'predict.html',{'prediction':classification})
