from django import forms
from django.core.validators import FileExtensionValidator
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import jobapply ,Job

class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only PDF files are allowed')]
    )

    class Meta:
        model = jobapply
        fields = ['username', 'email', 'cv', 'linked_url', 'github_url', 'coverlater']


class jobform(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
       model=Job
       fields=[ 'title','loction','company','salary_start','salary_end','description','vecancy','job_nature','experience','category']