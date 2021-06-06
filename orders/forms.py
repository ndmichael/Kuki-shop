from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div


class OrderForm(forms.ModelForm):
    design = forms.CharField(required=False)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
                
    #             Column('design', css_class='form-group col-md-6 mb-0'), 
    #             Column('postal_code', css_class='form-group col-md-6 mb-0'),

    #         ),        
    #         Row(
    #             Field('city', wrapper_class='form-group col-md-6 mb-0'),
    #             Field('address', wrapper_class='form-group col-md-6 mb-0'), 
    #             css_class='form-row'
    #         ),  

    #     )

    class Meta:
        model = Order
        fields =['first_name', 'last_name', 'email','design','postal_code',  'address',  'city' ]