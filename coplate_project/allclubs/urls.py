from django.urls import path
from . import views

urlpatterns = [
    path('allclubs/', views.allclubs, name='allclubs'),  # welcome.html 페이지 매핑
    path('clubs/', views.clubs, name='clubs'),   # work.html 페이지 매핑
    path('clubs/<int:todo_id>/', views.clubs, name='clubs_detail'),   # work.html 조회
]