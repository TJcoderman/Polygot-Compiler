from django.http import JsonResponse
from django.urls import path
from . import views

def api_root(request):
    return JsonResponse({
        'endpoints': {
            'detect_language': '/detect-language/',
            'run_code': '/run-code/',
            'ai_debug': '/ai-debug/'
        }
    })

urlpatterns =[
    path("compiler", views.main, name="main"),
    path("",views.index, name="index"),
    path("detect-language/", views.detect_language_view, name='detect_language'),
    path('ai-debug/', views.ai_debug_view, name='ai_debug'),
    path('run-code/', views.run_code_view, name='run_code')
]