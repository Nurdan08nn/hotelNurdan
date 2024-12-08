# Generated by Django 5.1.4 on 2024-12-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0002_hotel_description_ru_hotel_description_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='description_Ru',
            new_name='description_ru',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='name_Ru',
            new_name='name_ru',
        ),
        migrations.AddField(
            model_name='hotel',
            name='address_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='address_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='number_en',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='number_ru',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='status_en',
            field=models.CharField(choices=[('available', 'Available'), ('booked', 'Booked'), ('occupied', 'Occupied')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='status_ru',
            field=models.CharField(choices=[('available', 'Available'), ('booked', 'Booked'), ('occupied', 'Occupied')], max_length=20, null=True),
        ),
    ]
