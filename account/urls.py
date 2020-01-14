from django.urls import path
from .views import AccountsView, AuthView, HostAuthView, HostsView
urlpatterns = [
    path('', AccountsView.as_view()),
    path('/auth', AuthView.as_view()),
    path('/host', HostsView.as_view()),
    path('/host-auth', HostAuthView.as_view()),
]
