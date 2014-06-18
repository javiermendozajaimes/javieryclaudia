# -*- coding: utf-8 -*-
from ladon.server.wsgi import LadonWSGIApplication
from os.path import abspath,dirname,join

scriptdir = dirname(abspath(__file__))
service_modules = ['calculadora','palindromas','alumnos','materias','alumat','mat_estudiantes']

# Create the WSGI Application
application = LadonWSGIApplication(
	service_modules,
	[join(scriptdir,'services'),join(scriptdir,'appearance')],
	catalog_name = 'Servicios en Ladon',	
	catalog_desc = 'Los siguientes son los servicios existentes')

