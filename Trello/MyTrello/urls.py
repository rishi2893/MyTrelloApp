from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^records/$', views.data, name='data'),
    url(r'^(?P<board_id>[0-9]+)/$', views.board_detail, name='board_detail'),
    url(r'^(?P<board_id>[0-9]+)/(?P<card_id>[0-9]+)/$', views.card_detail, name='card_detail'),
]