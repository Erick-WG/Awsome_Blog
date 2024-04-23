from django.urls import path
#from . import views
from .views import CreateUserForm #, Logout

urlpatterns = [
    path('register/', CreateUserForm.as_view(), name="register"),
    # path('logout/', Logout.as_view(), name="logout"),
]
