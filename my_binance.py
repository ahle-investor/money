import pandas as pd
from datetime import datetime, timezone, timedelta
import calendar, os
import json
import datetime as dt              # working with dates
import requests
# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)