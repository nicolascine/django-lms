# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'cursos_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'cursos', ['Area'])

        # Adding model 'Curso'
        db.create_table(u'cursos_curso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Area'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'cursos', ['Curso'])

        # Adding model 'Unidad'
        db.create_table(u'cursos_unidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Curso'])),
        ))
        db.send_create_signal(u'cursos', ['Unidad'])

        # Adding model 'Clase'
        db.create_table(u'cursos_clase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Curso'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Unidad'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'cursos', ['Clase'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'cursos_area')

        # Deleting model 'Curso'
        db.delete_table(u'cursos_curso')

        # Deleting model 'Unidad'
        db.delete_table(u'cursos_unidad')

        # Deleting model 'Clase'
        db.delete_table(u'cursos_clase')


    models = {
        u'cursos.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cursos.clase': {
            'Meta': {'object_name': 'Clase'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Curso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Unidad']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cursos.curso': {
            'Meta': {'object_name': 'Curso'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Area']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cursos.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Curso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cursos']