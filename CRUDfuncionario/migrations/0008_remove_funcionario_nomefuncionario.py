# Generated by Django 4.2.9 on 2024-01-19 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDfuncionario', '0007_alter_funcionario_niveldeacesso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='nomeFuncionario',
        ),
    ]
