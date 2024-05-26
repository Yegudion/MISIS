# # blog/urls.py
# from django.urls import path
# # from .views import post_list, engineer_list
# from .views import  engineer_list


# urlpatterns = [
#     # path('', post_list, name='post_list'),
#     path('engineers/', engineer_list, name='engineer_list'),
# ]

# blog/urls.py

from django.urls import path
from .views import engineer_list, schedule_tasks

urlpatterns = [
    path('engineers/', engineer_list, name='engineer_list'),
    path('schedule/', schedule_tasks, name='schedule_tasks'),
]
