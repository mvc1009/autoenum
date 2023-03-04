from model.base import *

class Host(BaseDocument):
	meta = {
	'collection': 'ip_collection'
	}
	ip = db.StringField(required=True, unique=True)
	whois = db.StringField(default="null")
	#domains = db.ListField(db.ReferenceField("Domain"))

