from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boards/$', views.index_data, name='index_data'),
    url(r'^removed_boards/(?P<board_id>[0-9]+)$',views.remove_board, name='remove_board'),
    url(r'^removed_cards/(?P<card_id>[0-9]+)/$',views.remove_card, name='remove_card'),
    url(r'^removed_lists/(?P<list_id>[0-9]+)$',views.remove_list, name='remove_list'),
    url(r'^cards/(?P<board_id>[0-9]+)/$', views.board_data, name='board_data'),
    url(r'^lists/(?P<card_id>[0-9]+)/$', views.card_data, name='card_data'),
    url(r'^(?P<board_id>[0-9]+)/$', views.board_detail, name='board_detail'),
]