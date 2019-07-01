from django import forms

from .models import UploadFileModel
from .models import Photo


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)
