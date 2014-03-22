# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteSettings'
        db.create_table(u'core_sitesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('site_theme', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'core', ['SiteSettings'])


    def backwards(self, orm):
        # Deleting model 'SiteSettings'
        db.delete_table(u'core_sitesettings')


    models = {
        u'core.imagelinksection': {
            'Meta': {'object_name': 'ImageLinkSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.imagesection': {
            'Meta': {'object_name': 'ImageSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.page': {
            'Meta': {'ordering': "['weight']", 'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_home_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent_page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Page']", 'null': 'True', 'blank': 'True'}),
            'side_offset': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '64'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.sitesettings': {
            'Meta': {'object_name': 'SiteSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'site_theme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'core.textsection': {
            'Meta': {'object_name': 'TextSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['core']