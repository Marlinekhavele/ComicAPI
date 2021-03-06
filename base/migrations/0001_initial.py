# Generated by Django 3.0.5 on 2020-05-04 05:14

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name="Comic's title")),
                ('issue', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12)),
                ('pages', models.IntegerField(default=0, verbose_name='Pages')),
                ('authors', models.CharField(max_length=64, null=True, verbose_name='Author')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured', models.CharField(max_length=20)),
                ('latest', models.CharField(max_length=20)),
                ('trending', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Story title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='base.Character')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='base.Comic')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='base.Creator')),
            ],
        ),
        migrations.AddField(
            model_name='comic',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comic', to='base.Tag'),
        ),
    ]
