# Generated by Django 3.0.3 on 2020-03-04 06:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0003_auto_20200224_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="The water sport title as you'd like it to be seen by the public", max_length=255, verbose_name='title')),
                ('description', wagtail.core.fields.RichTextField(blank=True, help_text='Write some promotional copy', null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Water Sport image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'Water sports',
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.WaterSport'),
        ),
    ]
