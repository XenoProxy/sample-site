# Generated by Django 3.2.6 on 2021-08-08 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210807_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Rubric',
                'verbose_name_plural': 'Rubrics',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bd',
            options={'ordering': ['-published'], 'verbose_name': 'Advertisement', 'verbose_name_plural': 'Advertisements'},
        ),
        migrations.AlterField(
            model_name='bd',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='bd',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Rubric'),
        ),
    ]
