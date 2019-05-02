import re 
import sys 
import os
import time
from com.dtmilano.android.viewclient import ViewClient
from logger import logger
import pandas as pd

def pick_value(file_name, sheet_name, column_name, data_range):
	try:
		df = pd.read_excel(file_name, index_col=0, sheetname=sheet_name)
		column=df[column_name][data_range[0]:data_range[1]+1].tolist()
		assert len(column)!=0
		return column[0]
	except Exception as e:
		print(str(e))

import time
start_time = int(time.time())

flag = False
step_results = []
exception = []
exception_result = []
time_result = []

kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)
kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'debug': {}, 'startviewserver': True, 'compresseddump': True}
vc = ViewClient(device, serialno, **kwargs2)

filename = 'Demo#1'
try:
	vc.dump(window = -1)
except Exception as e:
	pass

