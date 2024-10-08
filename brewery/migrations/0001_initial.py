# Generated by Django 5.1 on 2024-08-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Malte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("origem", models.CharField(max_length=255)),
                ("fabricante", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("quantidade_max", models.IntegerField()),
                ("cor", models.IntegerField()),
                ("usar_mostura", models.BooleanField()),
                ("usar_fervura", models.BooleanField()),
                ("nao_fermentavel", models.BooleanField()),
                ("potencial_sg", models.FloatField()),
                ("aproveitamento", models.FloatField()),
                ("poder_diastatico", models.FloatField()),
                ("proteina", models.FloatField()),
                ("extrato_ibu", models.FloatField()),
                ("notas", models.TextField(blank=True, null=True)),
                ("ilustracao", models.CharField(blank=True, max_length=255, null=True)),
                ("preco", models.FloatField()),
            ],
        ),
    ]
