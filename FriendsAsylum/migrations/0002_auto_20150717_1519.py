# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FriendsAsylum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patiententry',
            name='age',
            field=models.CharField(default=b'', max_length=3, null=True, verbose_name=b'Age at Admittance', blank=True),
        ),
    ]
