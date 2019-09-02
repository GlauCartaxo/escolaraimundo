# Generated by Django 2.2.4 on 2019-09-02 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=5, verbose_name='nota')),
                ('data_avaliacao', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Aluno', verbose_name='nota_aluno')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AvaliacaoProAluno', to='users.Professor', verbose_name='nota_professor')),
            ],
        ),
    ]
