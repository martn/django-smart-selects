# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0005_merge"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_joined", models.DateField()),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="test_app.Group"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Talent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("persons", models.ManyToManyField(blank=True, to="test_app.Person")),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="writer",
            field=smart_selects.db_fields.ChainedManyToManyField(
                chained_field="publication",
                chained_model_field="publications",
                horizontal=True,
                to="test_app.Writer",
            ),
        ),
        migrations.AlterField(
            model_name="website",
            name="domains",
            field=smart_selects.db_fields.ChainedManyToManyField(
                chained_field="client",
                chained_model_field="client",
                to="test_app.Domain",
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="test_app.Person"
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="talents",
            field=smart_selects.db_fields.ChainedManyToManyField(
                chained_field="person",
                chained_model_field="persons",
                horizontal=True,
                to="test_app.Talent",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(
                through="test_app.Membership", to="test_app.Person"
            ),
        ),
    ]
