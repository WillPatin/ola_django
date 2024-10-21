# Generated by Django 5.1.1 on 2024-10-08 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0002_pessoa_delete_novamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tipo_pessoa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='primeiro_app.tipopessoa'),
        ),
    ]
