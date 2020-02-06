from django.db import models
from django.utils.html import format_html


class GithubUser(models.Model):
    login = models.CharField(max_length=256, unique=True)
    id = models.CharField(max_length=256, primary_key=True)
    node_id = models.CharField(max_length=256, unique=True)
    avatar_url = models.URLField()
    gravatar_id = models.CharField(max_length=256, blank=True)
    url = models.URLField()
    html_url = models.URLField()
    followers_url = models.URLField()
    following_url = models.URLField()
    gists_url = models.URLField()
    starred_url = models.URLField()
    subscriptions_url = models.URLField()
    organizations_url = models.URLField()
    repos_url = models.URLField()
    events_url = models.URLField()
    received_events_url = models.URLField()
    type = models.CharField(max_length=256)
    site_admin = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login

    def image(self):
        if self.avatar_url:
            return format_html('<img src="%s" />' % self.avatar_url)
        else:
            return '(Sin imagen)'
    image.short_description = 'Thumb'


class AllSearch(models.Model):
    text = models.CharField(max_length=256)
    min_followers = models.IntegerField(default=0)
    min_repository = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

