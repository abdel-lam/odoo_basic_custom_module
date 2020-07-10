# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
class Eleve(models.Model):
	_name= 'gestion.eleve'
	_description = u"Table des éléves"
	nume = fields.Char(string=u'Numéro de l étudiant', size=16, required=True)
	nome= fields.Char(string=u'Nom de l étudiant', size=32, required=True)
	nomc= fields.Char(string=u'Nom de la classe', size=32, required=True)
class Classe(models.Model):
	_name= 'gestion.classe'
	_description = u"Table des classe"
	nomc=fields.Char(string=u'Nom de la classe', size=32, required=True)		
class Professeur(models.Model):
	_name= 'gestion.professeur'
	_description = u"Table des professeur"
	nump=fields.Char(u'Numéro du prof', size=16, required=True)
	nomp=fields.Char(u'Nom du prof', size=32, required=True)
class Service(models.Model):
	_name= 'gestion.service'
	_description = u"Table des services"
	nump= fields.Integer(u'Numéro du prof', size=9, required=True)
	nomc=fields.Char(u'Nom de la classe', size=32, required=True)
	nbh=fields.Char(u'Nombre d heures assurés par un prof', digits=(9,4), required=True)