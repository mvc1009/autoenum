from model.base import *

class Host(BaseDocument):
	meta = {
	'collection': 'ip_collection'
	}
	ip = db.StringField(required=True, unique=True)
	whois = db.DictField()
	shodan = db.DictField()
	#domains = db.ListField(db.ReferenceField("Domain"))

