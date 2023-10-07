# # forms.py
# from django import forms
# from .models import Hr

# class HrForm(forms.ModelForm):
#     class Meta:
#         model = Hr
#         fields = ['date_of_birth']

#     date_of_birth = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'form-control datetimepicker', 'placeholder': 'yyyy-mm-dd'}),
#         input_formats=['%Y-%m-%d']  # Define the input date format
#     )

# forms.py
# from django import forms

# class DateForm(forms.Form):
#     selected_date = forms.DateField()
