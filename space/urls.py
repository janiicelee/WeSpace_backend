from django.urls import path
from .views import CategoryView, RecommendView, EditorView, DetailSpaceView
urlpatterns = [
    path('', CategoryView.as_view()),
    path('/recommend', RecommendView.as_view()),
    path('/editor', EditorView.as_view()),
    path('space/<int:space_id>', DetailSpaceView.as_view())
]
