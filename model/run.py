import boto3
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('example_write_s3')

bucket = 'projectjz'
key = 'ecs-example/sample.txt'
local_file_path = 'model/sample.txt'


if __name__ == "__main__":
    logger.info("writing {} -> {}".format(local_file_path, os.path.join(bucket, key)))

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)

    data = open(local_file_path, 'rb')
    bucket.put_object(Key=key, Body=data)
