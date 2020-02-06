from django.shortcuts import render
from django.views.generic import ListView
import requests
from . import forms
from .serializer import UserSearchSerializer
from .models import GithubUser, AllSearch
from django.utils import timezone
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
            min_followers = str(form.cleaned_data.get('min_followers'))
            min_repo = str(form.cleaned_data.get('min_repository'))
            AllSearch.objects.create(text=text, min_followers=min_followers, min_repository=min_repo)
            url = 'https://api.github.com/search/users?q='
            url += text
            url += '+repos:%3E'+min_repo
            url += '+followers:%3E'+min_followers
            r = requests.get(url)
            json = r.json()
            # print(json)
            serializer = UserSearchSerializer(data=json["items"], many=True)
            if serializer.is_valid():
                users = serializer.save()
                return render(request, 'search_user_display.html', {'users': users})
            print(serializer.instance)
        return render(request, self.template_name, {'form': form})
