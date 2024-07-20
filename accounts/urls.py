


from django.urls import path, re_path
from .views import *
from .models import *





from django.urls import path
from .views import contact_view, Contact_detail  # Make sure to import your views



app_name = 'accounts'

urlpatterns = [
    path('contact/', register_request, name='contact_view'),    # URL pattern for creating a contact
    path('<int:id>/detail/', Contact_detail, name='contact_detail'),  # URL pattern for contact detail view
    path('Login/', login_request,name='Login' ),
    path('logout',logout_request, name='logout'),

    # Add other URL patterns as needed
]