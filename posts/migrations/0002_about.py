# Generated by Django 4.0.1 on 2022-01-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField()),
                ('social_fb', models.CharField(blank=True, max_length=300, null=True)),
                ('social_yt', models.CharField(blank=True, max_length=300, null=True)),
                ('social_github', models.CharField(blank=True, max_length=300, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=300, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
