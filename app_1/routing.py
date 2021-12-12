from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path( r'^ws/stock/(?P<room_name>[^/]+)/$', consumers.StockConsumer.as_asgi()),
    re_path(r'ws/stock/(?P<room_name>\w+)/$', consumers.StockConsumer.as_asgi()),
    # r'^ws/stock/(?P<room_name>[^/]+)/$'
]








