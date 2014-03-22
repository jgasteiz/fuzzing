# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'core_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('in_navigation', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_home_page', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent_page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Page'], null=True, blank=True)),
            ('side_offset', self.gf('django.db.models.fields.CharField')(default='0', max_length=64)),
        ))
        db.send_create_signal(u'core', ['Page'])

        # Adding model 'ImageSection'
        db.create_table(u'core_imagesection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='one-whole', max_length=64)),
            ('alignment', self.gf('django.db.models.fields.CharField')(default='top', max_length=64)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Page'], null=True)),
        ))
        db.send_create_signal(u'core', ['ImageSection'])

        # Adding model 'ImageLinkSection'
        db.create_table(u'core_imagelinksection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='one-whole', max_length=64)),
            ('alignment', self.gf('django.db.models.fields.CharField')(default='top', max_length=64)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Page'], null=True)),
        ))
        db.send_create_signal(u'core', ['ImageLinkSection'])

        # Adding model 'TextSection'
        db.create_table(u'core_textsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='one-whole', max_length=64)),
            ('alignment', self.gf('django.db.models.fields.CharField')(default='top', max_length=64)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Page'], null=True)),
        ))
        db.send_create_signal(u'core', ['TextSection'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'core_page')

        # Deleting model 'ImageSection'
        db.delete_table(u'core_imagesection')

        # Deleting model 'ImageLinkSection'
        db.delete_table(u'core_imagelinksection')

        # Deleting model 'TextSection'
        db.delete_table(u'core_textsection')


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