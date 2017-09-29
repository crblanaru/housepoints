from django.conf.urls import url

from . import views

app_name = 'housepoints'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addpoints', views.PointsInsert.as_view(), name="addpoints"),
]
