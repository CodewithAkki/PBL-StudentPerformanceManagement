from django.urls import path
from achievementalInfo import views
urlpatterns = [
   
   #path('resetpassword/',views.resetPassoword),
    #path('resetpassword/<slug:uidb64>/<slug:token>',views.resetPasswordForm),
    #path('forgotPassoword/<str:email>',views.forgotPassoword),
    path('UpdateDestroyCertifications/<int:pk>',views.CertificationsViewAPI.as_view()),
    path('CertificationsAPIList',views.CertificationsAPIList.as_view()),
    path('UpdateDestroyGoals/<int:pk>',views.GoalsViewAPI.as_view()),
    path('GoalsAPIList',views.GoalsAPIList.as_view()),
    path('UpdateDestroyIntranship/<int:pk>',views.IntranshipViewAPI.as_view()),
    path('IntranshipAPIList',views.IntranshipAPIList.as_view()),
    path('UpdateDestroyPersonalAcheivement/<int:pk>',views.PersonalAcheivementViewAPI.as_view()),
    path('PersonalAcheivementAPIList',views.PersonalAcheivementAPIList.as_view()),
    path('UpdateDestroyPersonalProject/<int:pk>',views.PersonalProjectViewAPI.as_view()),
    path('PersonalProjectAPIList',views.PersonalProjectAPIList.as_view()),
    path('UpdateDestroyMilestones/<int:pk>',views.MilestonesViewAPI.as_view()),
    path('MilestonesAPIList',views.MilestonesAPIList.as_view()),
    ]