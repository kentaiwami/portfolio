from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ニックネームを入力', 'rows': '1'}))
    comment_text = forms.CharField(max_length=300, required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'コメントを入力', 'rows': '3'}))
