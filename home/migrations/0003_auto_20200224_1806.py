# Generated by Django 3.0.3 on 2020-02-24 18:06

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta',
            field=models.CharField(default='', help_text='Text to display on Call to Action', max_length=255, verbose_name='Hero CTA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta_link',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero CTA link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_text',
            field=models.CharField(default='', help_text='Write an introduction for the home page', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
