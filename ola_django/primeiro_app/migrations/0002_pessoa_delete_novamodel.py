from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('idade', models.IntegerField()),
                ('email', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='NovaModel',
        ),
    ]