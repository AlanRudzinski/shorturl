from django import forms
from .models import Shorting
# from django.core.validators import URLValidator


class URLForm(forms.ModelForm):

    # def clean(self):
    #     cleaned_data= super(URLForm, self).clean()

    class Meta:
        model = Shorting
        fields = ('url_in',)


# def validate_url(value):
#     url_validator = URLValidator()
#     try:
#         url_validator(value)
#     except:
#         raise forms.ValidationError("WRONG URL!")
#     return value
#
#
# class ValidateURLForm(forms.Form):
#     url = forms.CharField(label='Submit URL', validators=[validate_url])
#
#     def clean_url(self):
#         cleaned_url = super(ValidateURLForm, self).clean()
#         url = cleaned_url['url']
#         print(url)
#         url_validator = URLValidator()
#         try:
#             url_validator(url)
#         except:
#             raise forms.ValidationError("WRONG URL!")
#         return url
