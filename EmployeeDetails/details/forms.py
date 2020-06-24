from django import forms
class Details(forms.Form):
    topic = forms.CharField(max_length=200)
    explanation = forms.CharField(widget=forms.Textarea)