from django import forms
# import datetime


class Send_Article(forms.Form):
    Title = forms.CharField(label='Title', max_length=100)
    Body = forms.CharField(widget=forms.Textarea)
    # Date = forms.DateField(initial=datetime.date.today , disabled = True)