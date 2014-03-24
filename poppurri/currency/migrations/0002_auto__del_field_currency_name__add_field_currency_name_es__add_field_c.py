# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Currency.name'
        db.delete_column(u'currency_currency', 'name')

        # Adding field 'Currency.name_es'
        db.add_column(u'currency_currency', 'name_es',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Currency.name_en'
        db.add_column(u'currency_currency', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Currency', fields ['code']
        db.create_unique(u'currency_currency', ['code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Currency', fields ['code']
        db.delete_unique(u'currency_currency', ['code'])

        # Adding field 'Currency.name'
        db.add_column(u'currency_currency', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Deleting field 'Currency.name_es'
        db.delete_column(u'currency_currency', 'name_es')

        # Deleting field 'Currency.name_en'
        db.delete_column(u'currency_currency', 'name_en')


    models = {
        u'currency.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_es': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['currency']