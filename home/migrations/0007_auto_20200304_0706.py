# Generated by Django 3.0.3 on 2020-03-04 07:06

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200304_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sport_description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Enter the description for the water sport section on the home page.', null=True, verbose_name='Sport Section Description'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sport_title',
            field=models.CharField(blank=True, help_text='Enter the title for the water sport section on the home page.', max_length=255, verbose_name='Sport Section Title'),
        ),
    ]
