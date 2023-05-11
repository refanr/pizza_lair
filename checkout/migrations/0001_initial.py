# Generated by Django 4.2 on 2023-05-10 14:44


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(

            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('pizzas', models.ManyToManyField(to='pizza.pizza')),

                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]