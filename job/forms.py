from django import forms
from django.core.validators import FileExtensionValidator
from .models import jobapply



class jopapplyform(forms.ModelForm):
    cv =forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept':'.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='only pdf files')]

    )
    class Meta:
        model=jobapply
        fields=['username','email','cv','linked_url','github_url','coverlater']
