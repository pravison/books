# Generated by Django 4.2.4 on 2023-09-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_comments_comment_blog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments_count',
            field=models.IntegerField(blank=True, max_length=150, null=True),
        ),
    ]
