from django import forms
from django.core import validators

def check_for_Z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_Z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Re-enter email.")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_data = super().clean()
        email = all_data['email']
        vmail = all_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Email does not match.")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Bot Detected.")
    #     return botcatcher
