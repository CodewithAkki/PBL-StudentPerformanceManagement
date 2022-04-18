# Generated by Django 4.0.4 on 2022-04-18 03:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_customuser_bio_otpmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('SocialMediaId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('SocialMediaName', models.CharField(max_length=100)),
                ('SocialMediaLink', models.URLField()),
                ('PRN_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('LanguageId', models.AutoField(primary_key=True, serialize=False)),
                ('LanguageName', models.CharField(max_length=100)),
                ('Level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('PRN_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
