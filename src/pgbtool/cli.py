from argparse import ArgumentParser, Action
import sys

class driver_action(Action):

    def __call__(self, parser, driver, destination, namespace, values, option_strings=None):
        driver, destination = values
        amespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    # Initiating parser object
    parser = ArgumentParser(description='''
		PostgreSQL database backup tool (locally/AWS S3 bucket)
		''')

    # Adding Arguments
    parser.add_argument('url', help='PostgreSQL Database URL')
    parser.add_argument('--driver', '-d', metavar=("driver", "destination"), required=True,
                        nargs=2, action=driver_action)

    return parser


def main():
    import boto3
    from pgbtool import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)

    if args.driver == 's3':
        client = boto3.client('s3')
        print(f"Backing up to {args.destination} from S3 bucket")
        storage.s3(client, dump.stdout, args.destination, 'backup.sql')
    else:
        print(f"Backing up locally to {args.destination}")
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)
