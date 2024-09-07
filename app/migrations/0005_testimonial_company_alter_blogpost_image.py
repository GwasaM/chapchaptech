# Generated by Django 5.1 on 2024-08-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_churchnews_mail_teammember_testimonial_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=1, upload_to='blog_posts/'),
            preserve_default=False,
        ),
    ]
