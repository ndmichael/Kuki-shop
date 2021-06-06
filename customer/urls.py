from django.urls import path
from customer import views as c_view


app_name = 'customer'


urlpatterns = [
    path('', c_view.dashboard),

]