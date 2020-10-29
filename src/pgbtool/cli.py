from argparse import ArgumentParser, Action
import sys

class driver_action(Action):

	__call__(self, parser, driver, destination, namespace, values, option_strings=None):
	driver, destination = values
	namespace.driver = driver.lower()
	namespace.destination = destination


def create_parser():
	#Initiating parser object
	parser = ArgumentParser(description='''
		PostgreSQL database backup tool (locally/AWS S3 bucket)
		''')

	#Adding Arguments
	parser.add_argument('url', help='PostgreSQL Database URL')
	parser.add_argument('--driver', required=True, nargs=2, action=driver_action)

	return parser
