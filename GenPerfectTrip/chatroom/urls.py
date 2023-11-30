from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),
    path("hotels", views.hotels, name="hotels"),
    path("test", views.test, name="test"),
    path('generate', views.generate, name='generate'),
    path('improve', views.improve, name='improve'),
    path('test_generate', views.test_generate, name='test_generate'),
    path('test_improve', views.test_improve, name='test_improve'),
    path('hotels_generate', views.hotels_generate, name='hotels_generate'),
    path('hotels_improve', views.hotels_improve, name='hotels_improve')
]