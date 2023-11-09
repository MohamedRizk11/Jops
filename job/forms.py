from django import forms
from django.core.validators import FileExtensionValidator
from .models import jobapply

class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only PDF files are allowed')]
    )

    class Meta:
        model = jobapply
        fields = ['username', 'email', 'cv', 'linked_url', 'github_url', 'coverlater']

