import sys
import types
import pandas as pd
from botocore.client import Config
import ibm_boto3
import pickle

class DataLoader:
    
  def __init__(this, credentials):
    this.credentials = credentials
 
    this.client = ibm_boto3.client(service_name='s3',
        ibm_api_key_id=this.credentials['IBM_API_KEY_ID'],
        ibm_auth_endpoint=this.credentials['IBM_AUTH_ENDPOINT'],
        config=Config(signature_version='oauth'),
        endpoint_url=this.credentials['ENDPOINT'])

  def test_function(this):
    print(this.credentials)

  def load_order_details_1000_pkl(this):
    def __iter__(self): return 0
    body = this.client.get_object(
        this.credentials['BUCKET'],Key='order_details_1000.pkl')['Body']
    if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )
    return pickle.loads(body.read())