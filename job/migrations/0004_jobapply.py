# Generated by Django 4.2.6 on 2023-11-08 22:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_category_logo_alter_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.FileField(upload_to='cv')),
                ('linked_url', models.URLField(blank=True, help_text='please enter your linkedin profile', null=True)),
                ('github_url', models.URLField(blank=True, help_text='please enter your github profile', null=True)),
                ('coverlater', models.CharField(help_text='please enter your note here...', max_length=500)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job')),
            ],
        ),
    ]
