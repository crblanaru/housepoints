from django.conf.urls import url

from . import views

app_name = 'housepoints'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^addpoints', views.PointsInsert.as_view(), name="addpoints"),
    url(r'^all', views.ViewAllNonDeleted.as_view(), name="all"),
    url(r'^export', views.export_housepoints_csv, name="export"),
]
