from django.shortcuts import render
from polls.models import My_car
import joblib

# machine learning model
def prediction(request):
    mydata =  My_car.objects.all()
    khan = []
    
    for data in mydata:
        khan.append(data.Number_of_brakes)

    khang = list(map(int, khan))
    khang.reverse()
    print('The last element of list using reverse :', str(khang[0]))
    last_match = str(khang[0])

    # ML model
    distance = joblib.load('ML_finialzed_model.sav')
    ML_prediction = distance.predict([[last_match]])

    print('--------------------------------------')
    print('machine Learning prediction: ',ML_prediction)
    print('--------------------------------------')
    return render(request, 'polls/prediction.html', {'ML_prediction':ML_prediction})