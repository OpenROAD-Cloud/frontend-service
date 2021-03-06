# Generated by Django 2.0.7 on 2018-12-07 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openroad_uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='OpenROAD UUID')),
                ('name', models.CharField(max_length=20, verbose_name='Design Name')),
                ('repo_url', models.URLField(verbose_name='Repository URL')),
                ('imported_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Imported On')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Design',
                'verbose_name_plural': 'Designs',
            },
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openroad_uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='OpenROAD UUID')),
                ('triggered_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Triggered On')),
                ('started_on', models.DateTimeField(blank=True, null=True, verbose_name='Started On')),
                ('ended_on', models.DateTimeField(blank=True, null=True, verbose_name='Ended On')),
                ('commit_message', models.TextField(default='retrieving ..', verbose_name='Commit Message')),
                ('commit_id', models.CharField(default='retrieving ..', max_length=40, verbose_name='Commit ID')),
                ('live_monitoring_url', models.URLField(default='#', verbose_name='Live Monitor')),
                ('output_files_url', models.URLField(default='#', verbose_name='Output Files')),
                ('status', models.CharField(choices=[('triggered', 'triggered'), ('started', 'started'), ('completed', 'completed'), ('failed', 'failed')], default='triggered', max_length=10, verbose_name='Status')),
                ('status_message', models.TextField(blank=True, null=True, verbose_name='Status Message')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Design')),
            ],
            options={
                'verbose_name': 'Flow',
                'verbose_name_plural': 'Flows',
            },
        ),
    ]
