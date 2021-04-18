
from datetime import datetime
from django import forms
from .models import Budget, InOut


class RawBudgetForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    data = forms.DateTimeField(initial=datetime.now())


class RawBudgetListForm(forms.Form):
    id = forms.IntegerField()

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'description', 'data']
