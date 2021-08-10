from django import forms
from .models import (
    CSVUploadModel,
)


class CustomerCSVUploadModelForm(forms.ModelForm):
    """
    will be used to upload Customer data via CSV
    """

    class Meta:
        model = CSVUploadModel
        fields = [
            "upload_file",
        ]
        widgets = {
            "upload_file": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            )
        }
