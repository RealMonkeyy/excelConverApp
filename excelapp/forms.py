from django import forms
from .models import ConfigurationFile
import json

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ConfigurationFileForm(forms.ModelForm):
    class Meta:
        model = ConfigurationFile
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 20, 'cols': 80, 'style': 'white-space: pre;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            try:
                self.fields['content'].initial = json.dumps(json.loads(self.instance.content), indent=4, ensure_ascii=False)
            except (ValueError, TypeError):
                self.fields['content'].initial = self.instance.content