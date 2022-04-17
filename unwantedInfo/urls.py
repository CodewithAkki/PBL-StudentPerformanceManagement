from django.urls import path
from unwantedInfo import views
urlpatterns = [
    path('getcontrycode/',views.ImportCountryCode.as_view(),name='Allcontrycode')
]