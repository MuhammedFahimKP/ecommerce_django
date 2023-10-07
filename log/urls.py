from django.urls import path
from .  import  views

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('activate/<uidb64>/<token>',views.Activation.as_view(),name='activate'),
    path('signin/',views.SigninView.as_view(),name='signin'),
]
