# Generated by Django 4.2.1 on 2023-06-04 20:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enterarteapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id_event', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id_permission', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('restrictions', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('rol', models.CharField(max_length=15)),
                ('id_permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.permissions')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingOrder',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateTime', models.DateTimeField()),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.events')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.roles')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id_user_data', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='id_user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.userdata'),
        ),
        migrations.CreateModel(
            name='TransactionReport',
            fields=[
                ('id_report', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.events')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.shoppingorder')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ticket', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(limit_value=enterarteapp.models.generate_random_min_value), django.core.validators.MaxValueValidator(25000000)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('dateTime', models.DateTimeField()),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.events')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingorder',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.user'),
        ),
        migrations.AddField(
            model_name='roles',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.user'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.article')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.client')),
            ],
        ),
        migrations.AddField(
            model_name='permissions',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.user'),
        ),
        migrations.CreateModel(
            name='EventsData',
            fields=[
                ('id_event_data', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('photo', models.ImageField(default=None, upload_to='Galeria')),
                ('category', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('socialNetworks', models.CharField(max_length=20)),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.events')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='id_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.ticket', to_field='id_ticket'),
        ),
        migrations.AddField(
            model_name='events',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.user'),
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.article')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='enterarteapp.client'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='enterarteapp.CartDetail', to='enterarteapp.article'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterarteapp.category'),
        ),
    ]
