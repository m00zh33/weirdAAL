import boto3
import botocore

import json
import urllib
import logging
import sys,os
import pprint

pp = pprint.PrettyPrinter(indent=5, width=80)

from s3.s3 import *

#insert AWS key, will figure out how to pull this in from a single file for all scripts
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY =''

get_s3bucket_policy(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,'myfuckingbucket')