from django.urls import path
from .views import *
from .ajax_api import *

urlpatterns = [
    path('', Main.as_view(), name='get_to_main'),
    path('join/<slug:join_slug>', join_contribution, name='join_contribution'),
    path('tt/<int:ttid>', ShowTT.as_view(), name='show_TT'),
    path('rename/<int:ttid>', rename, name='rename_TT'),
    path('assign_contributor', assign_executor, name='assign_contributor'),
    path('delete_task', delete_task, name='delete_task'),
    path('execute_task', execute_task, name='execute_task'),
    path('check_task', check_task, name='check_task'),
    path('edit_desc', edit_desc_text, name='edit_desc')
]
