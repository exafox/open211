import csv
import IPython
import argparse

#Args
parser = argparse.ArgumentParser(description='Transform csv data to json Ohana/json spec.')
parser.add_argument('data_filename', metavar='data filename', type=str,help='csv file to parse (curated on opendatadc.org)')
parser.add_argument('mapper_filename', metavar='mapper filename', type=str,help='Mapped fieldnames (cureated on google docs)')
args = parser.parse_args()


#Read in data
data = list(csv.DictReader(open(args.data_filename)))

#Make field map
field_map = csv.DictReader(open(args.mapper_filename))
field_map = dict(((row['DC211'],row['Ohana']) for row in field_map))
reverse_field_map = dict(((v,k) for k,v in field_map.iteritems()))


class Organization(object):
	def __init__(self):
		self.locs = list()
		self.servs = list()
		self.urls = list()
	def hydrate(self,row):
		self.name = row['PublicName']





class Collection(object):
	def __init__(self):
		self.data = dict()

	def get_org(self,row):
		key = row['ResourceAgencyNum']
		if key in self.data:
			return data[key]
		else:
			self.data[key] = Organization()
		return self.data[key]



collection = Collection()
for row in data:

	row_has_service = row['TaxonomyLevelName'] == 'Program'
	row_has_location = True
	row_is_org = row['TaxonomyLevelName'] == 'Agency'

	org = collection.get_org(row)

	#If the row hold organization info use it to populate the organization fields
	if row_is_org:
		org.hydrate(row)

	if row_has_service:
		service = {
			'service_poc': row['Phone3Name']
			#map many more fields here

		}
		org.servs.append(service)

	if row_has_location:
		address = {
			'street': row['PhysicalAddress1'] + row['PhysicalAddress2'],
			'city': row['PhysicalCity'],
			'state': row['PhysicalStateProvince'],
			'zip': row['PhysicalPostalCode']
		}
		mail_address = {
			'street': row['MailingAddress1'] + row['MailingAddress2'],
			'city': row['MailingCity'],
			'state': row['MailingStateProvince'],
			'zip': row['MailingPostalCode']
		}
		location = {
			'address': address,
			'mail_address':mail_address
		}
		org.locs.append(location)


# Notes
#
# This code is just a start, there are a lot of fields not unpacked and no reserialization
# Some issues with the start dataset can be more gainfully fixed in the source data
# It would probably be better to have this as a rake task that imported to the database directly

