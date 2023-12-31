# Generated by Django 2.0.7 on 2018-08-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student_registration',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Full name (Bangla)'),
        ),
        migrations.AlterField(
            model_name='student_registration',
            name='relation_to_guardians',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Relation_to_guardians'),
        ),
    ]