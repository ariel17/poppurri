# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Mixture.name'
        db.delete_column(u'mixture_mixture', 'name')

        # Deleting field 'Mixture.long_description'
        db.delete_column(u'mixture_mixture', 'long_description')

        # Deleting field 'Mixture.short_description'
        db.delete_column(u'mixture_mixture', 'short_description')

        # Adding field 'Mixture.name_es'
        db.add_column(u'mixture_mixture', 'name_es',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mixture.name_en'
        db.add_column(u'mixture_mixture', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mixture.short_description_es'
        db.add_column(u'mixture_mixture', 'short_description_es',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mixture.short_description_en'
        db.add_column(u'mixture_mixture', 'short_description_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mixture.long_description_es'
        db.add_column(u'mixture_mixture', 'long_description_es',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mixture.long_description_en'
        db.add_column(u'mixture_mixture', 'long_description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Recipe.item'
        db.delete_column(u'mixture_recipe', 'item')

        # Adding field 'Recipe.item_es'
        db.add_column(u'mixture_recipe', 'item_es',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Recipe.item_en'
        db.add_column(u'mixture_recipe', 'item_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Mixture.name'
        db.add_column(u'mixture_mixture', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)

        # Adding field 'Mixture.long_description'
        db.add_column(u'mixture_mixture', 'long_description',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Adding field 'Mixture.short_description'
        db.add_column(u'mixture_mixture', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255),
                      keep_default=False)

        # Deleting field 'Mixture.name_es'
        db.delete_column(u'mixture_mixture', 'name_es')

        # Deleting field 'Mixture.name_en'
        db.delete_column(u'mixture_mixture', 'name_en')

        # Deleting field 'Mixture.short_description_es'
        db.delete_column(u'mixture_mixture', 'short_description_es')

        # Deleting field 'Mixture.short_description_en'
        db.delete_column(u'mixture_mixture', 'short_description_en')

        # Deleting field 'Mixture.long_description_es'
        db.delete_column(u'mixture_mixture', 'long_description_es')

        # Deleting field 'Mixture.long_description_en'
        db.delete_column(u'mixture_mixture', 'long_description_en')

        # Adding field 'Recipe.item'
        db.add_column(u'mixture_recipe', 'item',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'Recipe.item_es'
        db.delete_column(u'mixture_recipe', 'item_es')

        # Deleting field 'Recipe.item_en'
        db.delete_column(u'mixture_recipe', 'item_en')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'category.category': {
            'Meta': {'object_name': 'Category'},
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_final': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': u"orm['category.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mixture.mixture': {
            'Meta': {'object_name': 'Mixture'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mixtures'", 'null': 'True', 'to': u"orm['category.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'long_description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'long_description_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'short_description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'short_description_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'mixture.mixtureimage': {
            'Meta': {'object_name': 'MixtureImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'img/no-img.png'", 'max_length': '100'}),
            'mixture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['mixture.Mixture']"}),
            'outstanding': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'mixture.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'item_es': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mixture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'recipes'", 'to': u"orm['mixture.Mixture']"})
        }
    }

    complete_apps = ['mixture']