from django.urls import path
from .views import CategoryView, RecommendView, EditorView
urlpatterns = [
    path('', CategoryView.as_view()),
    path('/recommend', RecommendView.as_view()),
    path('/editor', EditorView.as_view()),
]
