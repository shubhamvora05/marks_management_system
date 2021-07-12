# Generated by Django 3.1.7 on 2021-07-11 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Standerd',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Std', models.PositiveIntegerField()),
                ('Medium', models.CharField(choices=[('CBSE', 'CBSE'), ('GSEB', 'GSEB'), ('Science', 'Science'), ('Commerce', 'Commerce')], default='GSEB', max_length=11)),
                ('Div', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_Name', models.CharField(max_length=30)),
                ('studentStd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marksApp.standerd')),
            ],
        ),
        migrations.CreateModel(
            name='studentInfo',
            fields=[
                ('HR_No', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('Middle_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Room_No', models.CharField(max_length=10)),
                ('studentStd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marksApp.standerd')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('totalMarks', models.PositiveIntegerField()),
                ('achivedMarks', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marksApp.studentinfo')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marksApp.subject')),
            ],
        ),
    ]