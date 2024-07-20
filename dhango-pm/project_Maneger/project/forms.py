from django import forms
from . import models
from django.utils.translation import gettext

attrs={
    "class":"form-control"
    }

class projectCreatForm(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=["category","title","descreption"]
        labels={
            'category':gettext("category"),
            'title':gettext('title'),
            'descreption':gettext('descreption')
        }
        widgets={
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'descreption':forms.Textarea(attrs=attrs)
}

class projectUpdateForm(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=["category","title","satutes"]
        widgets={
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'satutes':forms.Select(attrs=attrs)
}
