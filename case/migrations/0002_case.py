# Generated by Django 4.0.1 on 2022-02-09 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_point'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('view', models.IntegerField(default=0)),
                ('contact', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('skill', models.TextField(blank=True, null=True)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.amount')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.category')),
                ('mode', models.ManyToManyField(to='case.Mode')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.period')),
                ('respondent', models.ManyToManyField(to='user.Respondent')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.state')),
            ],
            options={
                'ordering': ['-createdon'],
            },
        ),
    ]
