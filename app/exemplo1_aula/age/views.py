from django.shortcuts import render
import json, datetime
from dateutil.relativedelta import relativedelta

def home(request):
    response = ''
    content = False
    if request.method == 'POST':
        _age = json.loads(request.POST.get("age"))
        birth = datetime.date(_age['y'],_age['m'],_age['d'])
        today = datetime.date.today()
        age = relativedelta(today,birth)

        if age.years >= 18:
            content = True
            response = 'Conte&uacute;do Liberado'
        else:
            response = 'D:<'

    return render(
        request,
        'index.html',
        {
            'r' : response,
            'content': content
        }
        ) 
