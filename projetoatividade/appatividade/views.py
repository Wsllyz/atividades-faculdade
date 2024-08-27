import requests
from django.http import JsonResponse
from django.shortcuts import render

def api_view(request):
    url = 'https://aps-atv2-production.up.railway.app/users'
    response = requests.get(url)

    if response.status_code == 200:
        data = {'nome': response.json()[-1]['firstName']}
        print(data)
        return render(request, 'index.html', data)
    else:
        return JsonResponse({'error': 'Erro ao acessar a API'}, status=response.status_code)
