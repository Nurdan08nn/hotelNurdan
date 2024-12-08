from modeltranslation.translator import register, TranslationOptions
from .models import Hotel, Room, Review


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('number', 'status')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)
