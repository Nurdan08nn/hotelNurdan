from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = [
        ('client', 'Client'),
        ('hotel_owner', 'Hotel Owner'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)


class Hotel(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name="hotels", on_delete=models.CASCADE)
    photos = models.ManyToManyField('HotelPhoto', related_name="hotel")

    def __str__(self):
        return self.name


class HotelPhoto(models.Model):
    image = models.ImageField(upload_to='hotel_photos/')


class Room(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('occupied', 'Occupied'),
    ]

    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.number} at {self.hotel.name}, Status: {self.status}, Price: {self.price}"


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')])

    def save(self, *args, **kwargs):
        if not self.pk:
            self.room.status = 'booked'
            self.room.save()
        super().save(*args, **kwargs)

    def cancel(self):
        self.room.status = 'available'
        self.room.save()
        self.delete()

    def __str__(self):
        return f"Booking for {self.room} by {self.user} from {self.start_date} to {self.end_date}"


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    class Meta:
        unique_together = ['user', 'hotel']
