#!/usr/bin/env python
from utils import *
from stratum import Stratum
from shared import Shared

shared = Shared()
print("Connecting to Stratum")
stratum = Stratum(shared.config.POOL_URL, shared.config.POOL_PORT)
print("Fetching Shares")
data = stratum.get_shares(shared.config.POOL_USER)
print("Storing Shares")
shared.store_shares(data)

