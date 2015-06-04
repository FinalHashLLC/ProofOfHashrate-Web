#!/usr/bin/env python
from crons.shared import Shared
import time

# Setup connection
print("Creating Connection")
shared = Shared()
session = shared.get_session()

# Drop existing tables and re-create
timer = 0
print("This Will WIPE ALL TABLES! Hit Ctrl-C to Cancel!")
while timer < 60:
   print("Wiping Tables in: {0}".format(60 - timer))
   timer += 1
   time.sleep(1)

print("Dropping Tables")
shared.models.Base.metadata.drop_all(shared.engine)
print("Creating Tables")
shared.models.Base.metadata.create_all(shared.engine)

