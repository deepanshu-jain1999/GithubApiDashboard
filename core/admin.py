from django.contrib import admin
from core import models


class GitHubUserAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False
    search_fields = ['login', 'created_at', 'updated_at']
    list_display = ('image', 'login', 'created_at', 'updated_at')
    # list_display_links = ('id', 'patient', 'booking_slot', 'token_number',)
    ordering = ('id',)

    class Meta:
        model = models.GithubUser


class AllSearchAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False
    search_fields = ['text', 'created_at', 'min_repository', 'min_repository']
    list_display = ('text', 'min_followers', 'min_repository', 'created_at')
    # list_display_links = ('id', 'patient', 'booking_slot', 'token_number',)
    ordering = ('id',)

    class Meta:
        model = models.AllSearch


admin.site.register(models.GithubUser, GitHubUserAdmin)
admin.site.register(models.AllSearch, AllSearchAdmin)
