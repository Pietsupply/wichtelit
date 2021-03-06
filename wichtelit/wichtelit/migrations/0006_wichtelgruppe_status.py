# Generated by Django 3.0.5 on 2020-04-12 08:33

from django.db import migrations
import django_enum_choices.choice_builders
import django_enum_choices.fields
import wichtelit.models


class Migration(migrations.Migration):

    dependencies = [
        ('wichtelit', '0005_auto_20200125_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='wichtelgruppe',
            name='status',
            field=django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('erstellt', 'erstellt'), ('gewürfelt', 'gewürfelt'), ('email_versendet', 'email_versendet')], default=wichtelit.models.Status['ERSTELLT'], enum_class=wichtelit.models.Status, max_length=15),
        ),
    ]
