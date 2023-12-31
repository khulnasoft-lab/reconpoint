# Generated by Django 2.1.1 on 2019-07-01 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0018_auto_20190529_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(blank=True, max_length=300, null=True)),
                ('training_place', models.CharField(blank=True, max_length=300, null=True)),
                ('training_duration', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Private'), ('2', 'Non-Private'), ('3', 'foreign')], max_length=120)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=300, null=True)),
                ('training_type', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='license_receive',
            name='permanent',
            field=models.BooleanField(blank=True, default=False, verbose_name='Permanent Address'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='present',
            field=models.BooleanField(blank=True, default=False, verbose_name='Present Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='allow_for_old_license_add',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='marital_status',
            field=models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Widow'), ('4', 'Divorce'), ('5', 'Separated')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='workingdetails',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.license_receive'),
        ),
        migrations.AddField(
            model_name='trainingdetails',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.license_receive'),
        ),
    ]