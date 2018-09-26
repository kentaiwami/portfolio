from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ニックネームを入力', 'rows': '1'}))
    text = forms.CharField(max_length=300, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'コメントを入力(必須)', 'rows': '3'}))
    id = forms.IntegerField(widget=forms.HiddenInput)
