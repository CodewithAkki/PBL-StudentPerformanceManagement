from django.urls import path
from ExaminationInfo import views
urlpatterns = [
   
   #path('resetpassword/',views.resetPassoword),
    #path('resetpassword/<slug:uidb64>/<slug:token>',views.resetPasswordForm),
    #path('forgotPassoword/<str:email>',views.forgotPassoword),
    path('UpdateDestroyDepatment/<int:pk>',views.ExaminationAPIView.as_view()),
    path('DepartmentAPIList',views.ExaminationAPIList.as_view()),
    path('UpdateDestroyCourses/<int:pk>',views.ExamAPIView.as_view()),
    path('CoursesAPIList',views.ExamAPIList.as_view()),
    path('UpdateDestroyTeachers/<int:pk>',views.ConductedOnView.as_view()),
    path('TeachersAPIList',views.CondutedOnAPIList.as_view()),

    ]