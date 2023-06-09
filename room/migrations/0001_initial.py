# Generated by Django 4.0.6 on 2023-05-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('room_type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('king', 'King')], max_length=10)),
                ('price', models.IntegerField()),
                ('room_image', models.ImageField(default='0.jpeg', upload_to='media')),
            ],
        ),
    ]
