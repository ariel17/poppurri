# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'currency_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'currency', ['Currency'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'currency_currency')


    models = {
        u'currency.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['currency']