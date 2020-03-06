from django.conf.urls import url
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from rooms.views import reservation_view


@hooks.register('register_admin_urls')
def urlconf_time():
    return [
        url(r'^reservations/$', reservation_view, name='reservations'),
    ]


@hooks.register('register_admin_menu_item')
def register_timeline_menu_item():
    return MenuItem(
        'Room Reservations',
        reverse('reservations'),
        classnames='icon icon-time',
        order=10000 # very last
    )
