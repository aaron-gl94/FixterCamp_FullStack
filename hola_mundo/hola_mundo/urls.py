from django.conf.urls import url
from django.contrib import admin
from Main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Sabado_2/$', views.Sabado.as_view()),
    url(r'^Style/$', views.ThugLife.as_view()),
    url(r'^PagWeb/$', views.PagWeb.as_view()),
]
