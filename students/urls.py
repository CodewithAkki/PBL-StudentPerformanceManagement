from django.urls import path
from students import views
urlpatterns = [
   
   #path('resetpassword/',views.resetPassoword),
    #path('resetpassword/<slug:uidb64>/<slug:token>',views.resetPasswordForm),
    #path('forgotPassoword/<str:email>',views.forgotPassoword),
    path('activation/<int:pk>/<int:sotp>',views.otpViewAPIView.as_view()),
    path('UserUpdateDelete/<int:pk>',views.userAPIView.as_view()),
    path('CreateGetUser/',views.usersList.as_view()),
    path('Password/',views.userpasswordupdate.as_view()),
    path('LanguagesUpdate/<int:pk>',views.LanguagesAPIView.as_view()),
    path('AddRetriveLanguages/',views.LanguagesList.as_view()),
    path('SocialMeidaUpdate/<int:pk>',views.SocialMediaAPIView.as_view()),
    path('AddRetriveSocialMedia/',views.SocialMediaList.as_view()),
    path('sendEmail/<str:email>/<str:body>',views.sendEmail.as_view()),
]