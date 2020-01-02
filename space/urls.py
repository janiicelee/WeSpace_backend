from django.urls import path
from .views import CategoryView, DetailSpaceView
urlpatterns = [
    path('', CategoryView.as_view()),
    path('space/<int:space_id>', DetailSpaceView.as_view())
]
