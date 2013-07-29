# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brewery'
        db.create_table('brewkeeper_brewery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('brewkeeper', ['Brewery'])

        # Adding model 'BeerStyle'
        db.create_table('brewkeeper_beerstyle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('genre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('ale', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('lager', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('brewkeeper', ['BeerStyle'])

        # Adding model 'Beer'
        db.create_table('brewkeeper_beer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('brewery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewkeeper.Brewery'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewkeeper.BeerStyle'])),
            ('ibu', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('abv', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('vintage', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('og', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fg', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('plato', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('degrees_lovibond', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal('brewkeeper', ['Beer'])


    def backwards(self, orm):
        # Deleting model 'Brewery'
        db.delete_table('brewkeeper_brewery')

        # Deleting model 'BeerStyle'
        db.delete_table('brewkeeper_beerstyle')

        # Deleting model 'Beer'
        db.delete_table('brewkeeper_beer')


    models = {
        'brewkeeper.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewkeeper.Brewery']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'degrees_lovibond': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ibu': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'og': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plato': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewkeeper.BeerStyle']"}),
            'vintage': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'brewkeeper.beerstyle': {
            'Meta': {'object_name': 'BeerStyle'},
            'ale': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lager': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        'brewkeeper.brewery': {
            'Meta': {'object_name': 'Brewery'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['brewkeeper']