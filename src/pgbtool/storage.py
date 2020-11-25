# Local backup
def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


# S3 bucket backup
def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
