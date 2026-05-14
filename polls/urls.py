from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # Cambiamos views.index por views.IndexView.as_view()
    path("", views.IndexView.as_view(), name="index"),
    
    # Cambiamos views.detail por views.DetailView.as_view()
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # Cambiamos views.results por views.ResultsView.as_view()
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # Este se queda igual porque 'vote' sigue siendo una función en views.py
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
