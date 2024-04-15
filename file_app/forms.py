from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Faculty, Department, Staff, AddFacultyDocument, AddStaffDocument


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name', 'middle_name', 'last_name', 'suffix_name', 'department', 'campus']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['code', 'name']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'middle_name', 'last_name',  'suffix_name', 'department', 'campus']

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class AddFacultyDocumentForm(forms.ModelForm):
    class Meta:
        model = AddFacultyDocument
        fields = ['subject', 'department', 'faculty', 'file_upload', 'campus']


class AddStaffDocumentForm(forms.ModelForm):

    class Meta:
        model = AddStaffDocument
        fields =  ['subject', 'department', 'staff', 'file_upload', 'campus']
        file_field = MultipleFileField()

