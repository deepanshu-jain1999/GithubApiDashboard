from django.shortcuts import render
from django.views.generic import ListView
import requests

from . import forms
from .serializer import UserSearchSerializer


# Create your views here.

class SearchUser(ListView):
    form_class = forms.UserSearchForm
    template_name = 'search_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            r = requests.get('https://api.github.com/search/users?q=' + text)
            json = r.json()
            print(json)
            serializer = UserSearchSerializer(data=json)
            if serializer.is_valid():
                users = serializer.save()
                return render(request, self.template_name, {'users': users})
        return render(request, 'search_user_display.html', {'form': form})


