from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "username": instance.username,
                "email": instance.email,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }


class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['image']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'address', 'owner', 'photos']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'number', 'status', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    rating = serializers.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = serializers.CharField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel', 'user', 'rating', 'comment']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:

        model = Booking
        fields = ['id', 'room', 'user', 'start_date', 'end_date', 'status']

    def validate(self, data):
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Дата выезда должна быть позже даты заезда.")

        room = data['room']
        existing_bookings = Booking.objects.filter(
            room=room,
            check_in_date__lt=data['check_out_date'],
            check_out_date__gt=data['check_in_date']
        )
        if existing_bookings.exists():
            raise serializers.ValidationError("Эта комната уже забронирована на выбранные даты.")

        return data