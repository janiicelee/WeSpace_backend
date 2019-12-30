# Generated by Django 3.0.1 on 2019-12-30 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_spaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Space_Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('amenity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Amenities')),
                ('space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
            ],
            options={
                'db_table': 'space_amenities',
            },
        ),
        migrations.AddField(
            model_name='spaces',
            name='amenity_space',
            field=models.ManyToManyField(through='space.Space_Amenities', to='space.Amenities'),
        ),
    ]
