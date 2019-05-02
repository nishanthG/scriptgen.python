import re 
import sys 
import os
import time
from com.dtmilano.android.viewclient import ViewClient
from logger import logger
# import pandas as pd

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

filename = 'Trial_1'
try:
	vc.dump(window = -1)
except Exception as e:
	pass


end = int(time.time())

try:
	total = end - start
	time_result.append(total)

except NameError as e:
	pass

if flag==0:
	pass

elif len(exception) > 0:
	step_results.append("Failed")
	exception_result.append(exception)
	exception = []

else:
	step_results.append("Passed")
	exception_result.append("None")
start = int(time.time())
flag=1

try:
	vc.findViewWithTextOrRaise('December 2018 arrow dropright').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('2').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass


end = int(time.time())

try:
	total = end - start
	time_result.append(total)

except NameError as e:
	pass

if flag==0:
	pass

elif len(exception) > 0:
	step_results.append("Failed")
	exception_result.append(exception)
	exception = []

else:
	step_results.append("Passed")
	exception_result.append("None")
start = int(time.time())
flag=1

try:
	vc.findViewWithTextOrRaise('ADD TIMESHEET').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass


end = int(time.time())

try:
	total = end - start
	time_result.append(total)

except NameError as e:
	pass

if flag==0:
	pass

elif len(exception) > 0:
	step_results.append("Failed")
	exception_result.append(exception)
	exception = []

else:
	step_results.append("Passed")
	exception_result.append("None")
start = int(time.time())
flag=1

try:
	vc.findViewWithTextOrRaise('Select Daystatus').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('WeeklyOffWorking').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('OK').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass


end = int(time.time())

try:
	total = end - start
	time_result.append(total)

except NameError as e:
	pass

if flag==0:
	pass

elif len(exception) > 0:
	step_results.append("Failed")
	exception_result.append(exception)
	exception = []

else:
	step_results.append("Passed")
	exception_result.append("None")
start = int(time.time())
flag=1

try:
	vc.findViewWithTextOrRaise('RESET').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewByIdOrRaise('dayStatus').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('WeeklyOff').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('OK').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass


end = int(time.time())

try:
	total = end - start
	time_result.append(total)

except NameError as e:
	pass

if flag==0:
	pass

elif len(exception) > 0:
	step_results.append("Failed")
	exception_result.append(exception)
	exception = []

else:
	step_results.append("Passed")
	exception_result.append("None")
start = int(time.time())
flag=1

try:
	vc.findViewWithTextOrRaise('arrow back').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('arrow back').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('arrow back').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass


end = int(time.time())

try:
	total = end - start
	time_result.append(total)

except NameError as e:
	pass

if flag==0:
	pass

elif len(exception) > 0:
	step_results.append("Failed")
	exception_result.append(exception)
	exception = []

else:
	step_results.append("Passed")
	exception_result.append("None")
start = int(time.time())
flag=1

logger(filename).generate_log()

logger(filename).add_test_info(Passed=step_results.count("Passed"), Failed=step_results.count("Failed"))

logger(filename).final_sequence(start_time,step_results,exception_result,time_result)