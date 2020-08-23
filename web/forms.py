from django import forms
from jdatetime import date,datetime


MONTH_CHOICES=[]
for i in range(len(date.j_months_short_en)):
    tup=(date.j_months_short_en[i],date.j_months_fa[i])
    MONTH_CHOICES.append(tup)


class AddBuyForm(forms.Form):
    name=forms.CharField(max_length=255,
                        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام نماد'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),
                            min_value=1)
    quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),
                                min_value=1)
    year=forms.IntegerField(initial=date.today().year,
                            max_value=date.today().year,
                            min_value=1381,
                            widget=forms.NumberInput(attrs={'class':'form-control'}))
    month=forms.ChoiceField(choices=MONTH_CHOICES,
                            initial=date.today().strftime("%b"),
                            widget=forms.Select(attrs={'class':'form-control'}))
    day=forms.IntegerField(initial=date.today().day,
                            max_value=31,
                            min_value=1,
                            widget=forms.NumberInput(attrs={'class':'form-control'}))
    
class AddSellForm(forms.Form):
    name=forms.CharField(max_length=255,
                        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام نماد'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),
                            min_value=1)
    quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),
                                min_value=1)
    year=forms.IntegerField(initial=date.today().year,
                            max_value=date.today().year,
                            min_value=1381,
                            widget=forms.NumberInput(attrs={'class':'form-control'}))
    month=forms.ChoiceField(choices=MONTH_CHOICES,
                            initial=date.today().strftime("%b"),
                            widget=forms.Select(attrs={'class':'form-control'}))
    day=forms.IntegerField(initial=date.today().day,
                            max_value=31,
                            min_value=1,
                            widget=forms.NumberInput(attrs={'class':'form-control'}))