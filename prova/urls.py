from django.contrib import admin
from django.urls import path
from app.views import home,create,store,plogin,dologin,dashboard,logouts,changePassword
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create),
    path('store/', store),
    path('plogin/', plogin),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('logouts/', logouts),
    path('password/', changePassword),
    
]
