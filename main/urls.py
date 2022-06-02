from django.urls import path
from . views import allsites,specificsite,addexperience,sitesperregion,map

urlpatterns=[

    path('allsites',allsites.as_view()),
    path('site/<str:pk>',specificsite.as_view()),
    path('addexperience/<str:pk>',addexperience.as_view()),
    path('perregion/<str:pk>',sitesperregion.as_view()),
    path('map/<str:pk>',map.as_view())
    ]
