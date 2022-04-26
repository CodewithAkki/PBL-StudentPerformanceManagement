from django.urls import path
from departmentalInfo import views
urlpatterns = [
   
   #path('resetpassword/',views.resetPassoword),
    #path('resetpassword/<slug:uidb64>/<slug:token>',views.resetPasswordForm),
    #path('forgotPassoword/<str:email>',views.forgotPassoword),
    path('UpdateDestroyDepatment/<int:pk>',views.DepatmentViewAPI.as_view()),
    path('DepartmentAPIList',views.DepartmentAPIList.as_view()),
    path('UpdateDestroyCourses/<int:pk>',views.CoursesView.as_view()),
    path('CoursesAPIList',views.CoursesAPIList.as_view()),
    path('UpdateDestroyTeachers/<int:pk>',views.TeachersView.as_view()),
    path('TeachersAPIList',views.TeachersAPIList.as_view()),

    ]