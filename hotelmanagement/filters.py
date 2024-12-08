import django_filters
from .models import Hotel, Room, Booking

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'name': ['icontains'],
            'address': ['icontains'],
            'owner': ['exact'],
        }

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = {
            'status': ['exact'],
            'hotel': ['exact'],
            'price': ['gte', 'lte'],
        }

class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = {
            'room': ['exact'],
            'user': ['exact'],
            'start_date': ['gte'],
            'end_date': ['lte'],
            'status': ['exact'],
        }
