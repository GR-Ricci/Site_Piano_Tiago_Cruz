from django.shortcuts import render
from django.http import HttpResponse

import os
from django.http import FileResponse, HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'piano/pages/index.html')

def about(request):
    return render(request, 'piano/pages/about.html')

def contact(request):
    return render(request, 'piano/pages/contact.html')

def classes(request):
    return render(request, 'piano/pages/classes.html')

#def usp(request):
    return render(request, 'piano/pages/usp.html')


def stream_video(request):
    # Tenta encontrar o caminho absoluto
    video_path = os.path.join(settings.BASE_DIR, 'static', 'piano', 'videos', 'index', 'instituto.mp4')

    # Se não encontrar, tenta o caminho dentro de um app (comum no Django)
    if not os.path.exists(video_path):
        # Substitua 'seu_app' pelo nome da pasta do seu aplicativo
        video_path = os.path.join(settings.BASE_DIR, 'piano', 'static', 'piano', 'videos', 'index', 'instituto.mp4')

    if os.path.exists(video_path):
        response = FileResponse(open(video_path, 'rb'), content_type='video/mp4')
        # Isso força o navegador a entender que pode pular o tempo
        response['Accept-Ranges'] = 'bytes'
        return response
    else:
        # Se falhar, ele vai te mostrar no navegador onde ele procurou
        return HttpResponse(f"Erro: Vídeo não encontrado. Procurei em: {video_path}", status=404)