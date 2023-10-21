from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

app_name = 'accounts'

urlpatterns = [
    path('sign-in/',
         LoginView.as_view(template_name='accounts/auth.html',
                           extra_context={'submit_text': 'Войти'}),
         name='sign-in'),
    path('sign-up/',
         CreateView.as_view(form_class=UserCreationForm,
                            template_name='accounts/auth.html',
                            success_url=reverse_lazy('accounts:sign-in'),
                            extra_context={'submit_text': 'Регистрация'}),
         name='sign-up')
]
