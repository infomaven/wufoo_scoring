# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table(u'wufoo_responder_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 11, 0, 0))),
            ('grade', self.gf('django.db.models.fields.IntegerField')()),
            ('data', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('auditName', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'wufoo_responder', ['Entry'])

        # Adding unique constraint on 'Entry', fields ['created', 'location', 'auditName']
        db.create_unique(u'wufoo_responder_entry', ['created', 'location', 'auditName'])

        # Adding model 'Item'
        db.create_table(u'wufoo_responder_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wufoo_responder.Entry'], null=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('response', self.gf('django.db.models.fields.TextField')()),
            ('failed', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'wufoo_responder', ['Item'])


    def backwards(self, orm):
        # Removing unique constraint on 'Entry', fields ['created', 'location', 'auditName']
        db.delete_unique(u'wufoo_responder_entry', ['created', 'location', 'auditName'])

        # Deleting model 'Entry'
        db.delete_table(u'wufoo_responder_entry')

        # Deleting model 'Item'
        db.delete_table(u'wufoo_responder_item')


    models = {
        u'wufoo_responder.entry': {
            'Meta': {'unique_together': "(('created', 'location', 'auditName'),)", 'object_name': 'Entry'},
            'auditName': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 11, 0, 0)'}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {})
        },
        u'wufoo_responder.item': {
            'Meta': {'object_name': 'Item'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wufoo_responder.Entry']", 'null': 'True'}),
            'failed': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'response': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['wufoo_responder']