# Generated by Django 4.2.7 on 2024-01-08 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0002_alter_patient_user'),
        ('doctor', '0004_review_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_type', models.CharField(choices=[('Pending', 'Pending'), ('Running', 'Running'), ('Completed', 'Completed')], default='Pending', max_length=30)),
                ('appointment_status', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=30)),
                ('symptoms', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime')),
            ],
        ),
    ]
