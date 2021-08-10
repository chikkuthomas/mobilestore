from django.urls import path
from customer import views
urlpatterns=[
    path("accounts/signin",views.SigninView.as_view(),name="signin"),
    path("accounts/signup",views.UserRegistrationView.as_view(),name="signup"),
    # path("accounts/signout",views.SignOutView.as_view(),name="signout"),
    path("home",views.CustomerHomeView.as_view(),name="custhome")
]