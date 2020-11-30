from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'), 
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('design', css_class='form-group col-md-6 mb-0'), 

            ), 'address',        
            Row(
                Field('postal_code', wrapper_class='form-group col-md-6 mb-0'),
                Field('city', wrapper_class='form-group col-md-6 mb-0'), 
                css_class='form-row'
            ),  
            Submit('submit', 'COMPLETE ORDER', css_class="btn btn-lg mt-3")

        )

    class Meta:
        model = Order
        fields =['first_name', 'last_name', 'email', 'design', 'address', 'postal_code', 'city']