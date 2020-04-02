from odm2api.ODMconnection import dbconnection
import odm2api.services.readService as odm2rs
import odm2api.ODM2.services as sv
# -----------------------------------------------------
# 1. A ODM2 controlled vocabulary (CV) import:
# python ./cvload.py postgresql://postgres:odm2@localhost:5432/postgres

# 2. A server-based database system connection
db_credentials = {
    'address': 'localhost:5432',
    'db': 'postgres',
    'user': 'postgres',
    'password': 'odm2'
}
session_factory = dbconnection.createConnection('postgresql',
                                                **db_credentials)
read = odm2rs.ReadODM2(session_factory)

#---------------------------------------------------------



DBSession = session_factory.getSession()

l1 = read.getPeople(firstname="john")

from odm2api.models import (Methods, Models, People,
                            ProcessingLevels, RelatedModels, Variables)

    # create some people
p1 = People(PersonFirstName='Peter', PersonLastName='Silie')
p2 = People(PersonFirstName='tony', PersonLastName='castronova')
p3 = People(PersonFirstName='john', PersonLastName='doe')

sv.createService.CreateODM2(session_factory).createPerson(p1)


from odm2api import serviceBase
sv.deleteService.DeleteODM2(session_factory).remove(l1[0])

readCVs = read.getCVs("Variable Name")