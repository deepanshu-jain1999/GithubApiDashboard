from django import forms


class UserSearchForm(forms.Form):
    text = forms.CharField(max_length=256)
    min_followers = forms.IntegerField(initial=0)
    min_repository = forms.IntegerField(initial=0)

    class Meta:
        fields = '__all__'
