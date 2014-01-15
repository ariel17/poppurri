# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Category.slug'
        db.delete_column(u'category_category', 'slug')

        # Adding field 'Category.slug_es'
        db.add_column(u'category_category', 'slug_es',
                      self.gf('django.db.models.fields.SlugField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.slug_en'
        db.add_column(u'category_category', 'slug_en',
                      self.gf('django.db.models.fields.SlugField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Category.slug'
        db.add_column(u'category_category', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'Category.slug_es'
        db.delete_column(u'category_category', 'slug_es')

        # Deleting field 'Category.slug_en'
        db.delete_column(u'category_category', 'slug_en')


    models = {
        u'category.category': {
            'Meta': {'object_name': 'Category'},
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_final': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': u"orm['category.Category']"}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug_es': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['category']