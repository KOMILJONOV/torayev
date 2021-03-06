# Generated by Django 4.0.5 on 2022-07-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='media/')),
                ('media_type', models.IntegerField(choices=[(0, 'Text'), (1, 'Photo'), (2, 'Video'), (3, 'Audio'), (4, 'Document')])),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('chat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_registered', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
