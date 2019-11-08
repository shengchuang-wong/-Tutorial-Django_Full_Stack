from django import forms
from django.core import validators

def check_for_z(value):
  if value[0].lower() != 'z':
    raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
  name = forms.CharField(validators=[check_for_z])
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Enter your email again:')
  text = forms.CharField(widget=forms.Textarea)
  botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

  def clean(self):
    all_clean_data = super().clean() # get data from entire form
    email = all_clean_data['email']
    vmail = all_clean_data['verify_email']

    if email != vmail:
      raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if len(botcatcher) > 0:
  #     raise forms.ValidationError("GOTCHA BOT!")
  #   return botcatcher