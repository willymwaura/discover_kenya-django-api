from django.urls import path
from.import views
from . views import Tasklist,deletetask

urlpatterns = [
path('tasklist',Tasklist.as_view()),
path('deletetask/<int:pk>',deletetask.as_view()),    
]
