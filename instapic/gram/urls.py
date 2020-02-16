from django.urls import path, include

''' 
This is to allow us to connect the PROJECT's  url with this APP's url 
it will then allow us to define paths here as we had included (grams urls)
in the PROJECT.
'''

from . import views

'''
Here we are importing the views as we shall connect templates from there 
'''

from django.conf import settings

'''
This is importing the settings configurations to (gramapp)
'''

from django.conf.urls.static import static

'''
This is to import static-files in urls
'''
from django.shortcuts import render, redirect

from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)

'''End Of Import'''
# ---------------------------------------------------------------------#

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('explore', views.explore, name='explore'),
    path('notification', views.notification, name='notification'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''