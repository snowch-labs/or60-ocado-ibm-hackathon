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
    
  def _load_pickle(this, filename):
    def __iter__(self): return 0
    body = this.client.get_object(
        Bucket=this.credentials['BUCKET'],
        Key=filename
        )['Body']
    if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )
    return pickle.loads(body.read())

  def load_order_details_1000(this):
    return this._load_pickle('order_details_1000.pkl')

  def load_ordered_skus(this):
    return this._load_pickle('ordered_skus.pkl')
