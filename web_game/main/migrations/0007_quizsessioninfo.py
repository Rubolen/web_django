# Generated by Django 5.0.4 on 2024-05-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSessionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_question_id', models.CharField(max_length=50, verbose_name='Id текущего вопроса')),
                ('session_score', models.CharField(max_length=50, verbose_name='Количество очков')),
            ],
        ),
    ]
