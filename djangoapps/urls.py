from django.urls import path,re_path
from djangoapps import views
app_name='djangoapps'
urlpatterns = [
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
]