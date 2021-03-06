# Generated by Django 4.0.3 on 2022-04-27 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCommune', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDistrict', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('KindOfHouse', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('legalDocuments', models.CharField(max_length=100)),
                ('Area', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('Commune', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.commune')),
                ('District', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.district')),
            ],
        ),
        migrations.CreateModel(
            name='HouseLessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameLessor', models.CharField(max_length=100)),
                ('Sex', models.CharField(max_length=10)),
                ('PhoneNumber', models.CharField(default='', max_length=15)),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertiesEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProvince', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameServiceFirst', models.CharField(max_length=100, null=True)),
                ('QuatityFirst', models.IntegerField()),
                ('nameServiceSecond', models.CharField(max_length=100, null=True)),
                ('QuatitySecond', models.IntegerField()),
                ('nameServiceThird', models.CharField(max_length=100, null=True)),
                ('QuatityThird', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TopProvince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FooterImage', models.ImageField(upload_to='images/', verbose_name='')),
                ('nameProvince', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.province')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('House', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.house')),
                ('Service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.service')),
            ],
        ),
        migrations.CreateModel(
            name='ImageHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkImageFirst', models.ImageField(null=True, unique=True, upload_to='images/', verbose_name='')),
                ('LinkImageSecond', models.ImageField(null=True, unique=True, upload_to='images/', verbose_name='')),
                ('LinkImageThird', models.ImageField(null=True, unique=True, upload_to='images/', verbose_name='')),
                ('LinkImageFourth', models.ImageField(null=True, unique=True, upload_to='images/', verbose_name='')),
                ('LinkImageFifth', models.ImageField(null=True, unique=True, upload_to='images/', verbose_name='')),
                ('NoteImage', models.CharField(max_length=100)),
                ('House', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.house')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='HouseLessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.houselessor'),
        ),
        migrations.AddField(
            model_name='house',
            name='Province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.province'),
        ),
    ]
