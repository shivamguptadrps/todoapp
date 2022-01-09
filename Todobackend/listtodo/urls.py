from django.conf.urls import url
from . import views
from . import cricket
app_name = 'globivacppapp'

urlpatterns = [
    url(r'^test/$', cricket.getCricket),
    url(r'^gettodo/$', views.todoapi),
    url(r'^gettododelete/$', views.todoapidelete),
    url(r'^gettodo/[0-9]/$', views.todoapi)

    ]

