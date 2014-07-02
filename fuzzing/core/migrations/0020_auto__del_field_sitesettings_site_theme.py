# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SiteSettings.site_theme'
        db.delete_column(u'core_sitesettings', 'site_theme')


    def backwards(self, orm):
        # Adding field 'SiteSettings.site_theme'
        db.add_column(u'core_sitesettings', 'site_theme',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    models = {
        u'core.backgroundimagetextsection': {
            'Meta': {'object_name': 'BackgroundImageTextSection'},
            'background_position': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_color': ('django.db.models.fields.CharField', [], {'default': "'#000000'", 'max_length': '64'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_side': ('django.db.models.fields.CharField', [], {'default': "'left'", 'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.imagelinksection': {
            'Meta': {'object_name': 'ImageLinkSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'offset': ('django.db.models.fields.CharField', [], {'default': "'no-offset'", 'max_length': '64'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'subtitle_ca': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'subtitle_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'subtitle_es': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'subtitle_eu': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'subtitle_fr': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.imagesection': {
            'Meta': {'object_name': 'ImageSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'offset': ('django.db.models.fields.CharField', [], {'default': "'no-offset'", 'max_length': '64'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.page': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_home_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_long_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'left_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'left_text_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'left_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'left_text_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'left_text_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'left_text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parent_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'redirect_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'redirect'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'right_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'right_text_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'right_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'right_text_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'right_text_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'right_text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'show_share': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_social_icons': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'side_offset': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '64'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.separatorsection': {
            'Meta': {'object_name': 'SeparatorSection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.sitesettings': {
            'Meta': {'object_name': 'SiteSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'core.textsection': {
            'Meta': {'object_name': 'TextSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'offset': ('django.db.models.fields.CharField', [], {'default': "'no-offset'", 'max_length': '64'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.videosection': {
            'Meta': {'object_name': 'VideoSection'},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '64'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'360px'", 'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'one-whole'", 'max_length': '64'}),
            'offset': ('django.db.models.fields.CharField', [], {'default': "'no-offset'", 'max_length': '64'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Page']", 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '256', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['core']