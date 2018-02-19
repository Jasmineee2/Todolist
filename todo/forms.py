from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length = 40,
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
                'area-label': 'Todo', 'area-describedby': 'add-btn'}))
