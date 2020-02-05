from django import forms


class UserSearchForm(forms.Form):
    text = forms.CharField(max_length=256)

    class Meta:
        fields = ['test']
