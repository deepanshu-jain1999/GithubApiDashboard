from django.contrib import admin
from core import models

class GitHubUserAdmin(admin.ModelAdmin):
    search_fields = ['login', 'created_at']
    list_display = ('image', 'login', 'created_at')
    # list_display_links = ('id', 'patient', 'booking_slot', 'token_number',)
    ordering = ('id',)

    class Meta:
        model = models.GithubUser


admin.site.register(models.GithubUser, GitHubUserAdmin)
