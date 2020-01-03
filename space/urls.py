from django.urls import path
from .views import CategoryView, RecommendView, EditorView, DetailSpaceView, Registration, Reservation
urlpatterns = [
    path('', CategoryView.as_view()),
    path('/recommend', RecommendView.as_view()),
    path('/reservation', Reservation.as_view()),
    path('/editor', EditorView.as_view()),
    path('/registration', Registration.as_view()),
    path('/<int:space_id>', DetailSpaceView.as_view())
]
