from django import forms
from django.forms import ModelForm
from .models import *

class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms. CharField(max_length=100)
    email = forms.EmailField()

class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)

class SolicitudesStep1_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step1
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 1'
        label='Solicitudes: Step 1'

class SolicitudesStep1b_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step1b
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 1b'
        label='Solicitudes: Step 1b'

class SolicitudesStep2_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2'
        label='Solicitudes: Step 2'

class SolicitudesStep2b_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2b
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2b'
        label='Solicitudes: Step 2b'

class SolicitudesStep2c_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2c
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2c'
        label='Solicitudes: Step 2c'

class SolicitudesStep2d_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2d
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2d'
        label='Solicitudes: Step 2d'

class SolicitudesStep2e_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2e
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2e'
        label='Solicitudes: Step 2e'

class SolicitudesStep2f_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2f
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2f'
        label='Solicitudes: Step 2f'

class SolicitudesStep3_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step3
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 3'
        label='Solicitudes: Step 3'

class SolicitudesStep4a_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4a
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4a'
        label='Solicitudes: Step 4a'

class SolicitudesStep4b_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4b
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4b'
        label='Solicitudes: Step 4b'

class SolicitudesStep4c_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4c
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4c'
        label='Solicitudes: Step 4c'

class SolicitudesStep4d_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4d
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4d'
        label='Solicitudes: Step 4d'

class SolicitudesStep4e_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4e
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4e'
        label='Solicitudes: Step 4e'

class SolicitudesStep4f_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4f
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4f'
        label='Solicitudes: Step 4f'

class SolicitudesStep4g_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step4g
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 4g'
        label='Solicitudes: Step 4g'

class SolicitudesStep5_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step5
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 5'
        label='Solicitudes: Step 5'

class SolicitudesStep6a_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step6a
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 6a'
        label='Solicitudes: Step 6a'

class SolicitudesStep6b_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step6b
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 6b'
        label='Solicitudes: Step 6b'

class SolicitudesStep7_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step7
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 7'
        label='Solicitudes: Step 7'