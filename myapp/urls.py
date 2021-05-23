from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('aguywhosucksatvalorant/',views.YASH),
    path('', views.main),
    path('Signup/',views.showteacher),
    path('ShowTeacherDetails/',views.showteacherdetails),
    path('searchTeacher/',views.searchTeacher),
    path('<int:id>/updateTeacher',views.updateTeacher),
    path('<int:id>/',views.viewTeacher),

]