# Generated by Django 4.0.1 on 2022-02-18 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='state',
            field=models.ForeignKey(default='新進案', null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.state'),
        ),
    ]
