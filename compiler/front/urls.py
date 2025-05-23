from django.http import JsonResponse
from django.urls import path
from . import views

def api_root(request):
    return JsonResponse({
        'endpoints': {
            'detect_language': '/detect-language/',
            'run_code': '/run-code/',
            'ai_debug': '/ai-debug/',
            'ai_explain': '/ai-explain/',
            'ai_review': '/ai-review/',
            'ai_fix': '/ai-fix/',
            'ai_optimize': '/ai-optimize/',
            'ai_complete': '/ai-complete/',
            'ai_translate': '/ai-translate/'
        }
    })

urlpatterns = [
    path("compiler", views.main, name="main"),
    path("", views.index, name="index"),
    path("detect-language/", views.detect_language_view, name='detect_language'),
    path('ai-debug/', views.ai_debug_view, name='ai_debug'),
    path('run-code/', views.run_code_view, name='run_code'),
    # New AI endpoints
    path('ai-explain/', views.ai_explain_code, name='ai_explain'),
    path('ai-review/', views.ai_review_code, name='ai_review'),
    path('ai-fix/', views.ai_fix_code, name='ai_fix'),
    path('ai-optimize/', views.ai_optimize_code, name='ai_optimize'),
    path('ai-complete/', views.ai_complete_code, name='ai_complete'),
    path('ai-translate/', views.ai_translate_code, name='ai_translate'),
    path('ai-complexity/', views.ai_complexity_analysis, name='ai_complexity'),
]