from django.shortcuts import render

from rooms.models import Reservations


def reservation_view(request):
    reservations = Reservations.objects.select_related('room').all()
    return render(request, "rooms/list.html", {'title': 'Reservations', 'reservations': reservations})
