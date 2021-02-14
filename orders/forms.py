from django import forms
from .models import Order, Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

class CustomerForm(forms.ModelForm) :
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('first_name', css_class='form-group col-md-6 mb-0'),
    #             Column('last_name', css_class='form-group col-md-6 mb-0'), 
    #             css_class='form-row'
    #         ), 'email'
    # )
    class Meta:
        model = Customer
        fields =['first_name', 'last_name', 'email']


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
        fields =['design','postal_code',  'address',  'city' ]