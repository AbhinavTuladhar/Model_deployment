from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'model/home.html')

def results(request):
    model = joblib.load('finalised_model.sav')
    
    parameters = dict()
    columns = list()
    data = list()

    parameters['SeniorCitizen'] = request.POST.get('SeniorCitizen')
    parameters['Partner'] = request.POST.get('Partner')
    parameters['Dependents'] = request.POST.get('Dependents')
    parameters['tenure'] = int(request.POST.get('tenure'))
    parameters['PhoneService'] = request.POST.get('PhoneService')
    parameters['MultipleLines'] = request.POST.get('MultipleLines')
    parameters['InternetService'] = request.POST.get('InternetService')
    parameters['OnlineSecurity'] = request.POST.get('OnlineSecurity')
    parameters['OnlineBackup'] = request.POST.get('OnlineBackup')
    parameters['DeviceProtection'] = request.POST.get('DeviceProtection')
    parameters['TechSupport'] = request.POST.get('TechSupport')
    parameters['StreamingTV'] = request.POST.get('StreamingTV')
    parameters['StreamingMovies'] = request.POST.get('StreamingMovies')
    parameters['Contract'] = request.POST.get('Contract')
    parameters['PaperlessBilling'] = request.POST.get('PaperlessBilling')
    parameters['PaymentMethod'] = request.POST.get('PaymentMethod')
    parameters['MonthlyCharges'] = int(request.POST.get('MonthlyCharges'))

    for key, item in parameters.items():
        columns.append(key)
        data.append(item)

    dummy = pd.DataFrame([data], columns = columns)
    prediction = model.predict(dummy)
    prediction_prob = model.predict_proba(dummy)
    print(prediction[0])

    to_return = {
        'predicted_class' : prediction[0],
        'churn_prob' : round(prediction_prob[0][1], 4) * 100
    }

    return render(request, 'model/results.html', to_return)
