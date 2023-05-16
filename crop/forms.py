from django import forms
from .models import CropImage

class CreateCropImageMutationForm(forms.ModelForm):
    class Meta:
        model = CropImage
        fields = [
            "name",
            "logo",
            "crop",
        ]