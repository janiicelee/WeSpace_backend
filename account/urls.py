from django.urls import path
from .views      import AccountsView, AuthView, Decorator
urlpatterns = [
     path('', AccountsView.as_view()),
     path('/auth', AuthView.as_view()),
     path('/a', Decorator.as_view())
]
