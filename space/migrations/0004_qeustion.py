# Generated by Django 3.0.1 on 2019-12-29 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_hosts'),
        ('space', '0003_spaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qeustion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Accounts')),
            ],
        ),
    ]
