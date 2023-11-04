from django import forms
from .models import FormData
from .models import Material
from django.db import models
from django import forms
from .models import FormData, Department, Course

class FormDataForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    class Meta:
        model = FormData
        fields = '__all__'
        
    materials_provided = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),
    )
    
    course = forms.ModelChoiceField(queryset=Course.objects.none())

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set
        
        
        
        

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),
    )
    course = forms.ModelChoiceField(queryset=Course.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set
    
    
