from django.shortcuts import render
import json, datetime
from dateutil.relativedelta import relativedelta

def home(request):
    _class = ''
    response = ''
    content = False
    if request.method == 'POST':
        _age = request.POST.get('age')
        if len(_age) == 10:
            birth = datetime.date.fromisoformat(_age)
            today = datetime.date.today()
            age = relativedelta(today,birth)

            if age.years >= 18:
                content = True
                response = 'Conteúdo Liberado'
                _class = 'response'
            else:
                _class = 'evil'
                response = 'D:<'

    return render(
        request,
        'index.html',
        {
            'response' : response,
            'content': content,
            'r_class': _class
        }
        ) 
