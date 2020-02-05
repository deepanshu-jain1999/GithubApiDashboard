from django.db import models


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
