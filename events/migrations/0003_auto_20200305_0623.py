# Generated by Django 3.0.3 on 2020-03-05 06:23

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200305_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='promo_line',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='A short promo line of the event.', verbose_name='Promo Line'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='A short description of the event.', verbose_name='Description'),
        ),
    ]