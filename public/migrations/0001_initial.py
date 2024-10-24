# Generated by Django 5.1.1 on 2024-10-22 10:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('no', '-------'), ('ngo', 'Non-governmental organization'), ('npo', 'Non-profit organization'), ('govs', 'Governmental organization'), ('others', 'Others')], default='no', max_length=100)),
                ('type_of_service', models.CharField(choices=[('NO', '-------'), ('PM', 'Project Management'), ('RP', 'Research and Policy Development'), ('DA', 'Data Analysis and Management'), ('ME', 'Monitoring and Evaluation'), ('SE', 'Stakeholder Engagement and Advocacy'), ('CB', 'Capacity Building and Training'), ('OT', 'Others')], default='NO', max_length=2)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('project_title', models.CharField(max_length=500)),
                ('project_description', models.TextField(default='Describe in few words...', max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_sector', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-type_of_service'], name='public_publ_type_of_1135f4_idx')],
            },
        ),
    ]
