# Generated by Django 3.0.3 on 2020-03-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_agent_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign_Model',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('aid', models.IntegerField()),
            ],
        ),
    ]
