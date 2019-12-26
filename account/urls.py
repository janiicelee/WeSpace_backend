from django.urls import path
from .views      import AccountsView, AuthView
urlpatterns = [
     path('', AccountsView.as_view()),
     path('/auth', AuthView.as_view())
]
