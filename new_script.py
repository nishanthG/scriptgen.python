import re 
import sys 
import os
import time
from com.dtmilano.android.viewclient import ViewClient
from logger import logger
import pandas as pd

def pick_value(file_name, column_name):
	df = pd.read_excel(file_name, index_col=0)
	assert len(df[column_name].tolist())!=0
	return df[column_name].tolist()[0]

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
	vc.findViewWithTextOrRaise('7').touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	value = pick_value("/media/gn/Work/AQM/PY_RepV2.0/logsample.xlsx")
	vc.findViewWithTextOrRaise(value).touch()
	vc.sleep(3)
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

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
	vc.findViewWithTextOrRaise('Select Daystatus').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('Absent').touch()
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

try:
	vc.findViewWithTextOrRaise('Select Client').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('Aditya Birla').touch()
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
	vc.findViewWithTextOrRaise('Select Project').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('Aditya Birla New').touch()
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
	vc.findViewWithTextOrRaise('Select Module').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('NSE Now 2.0 - General').touch()
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
	vc.findViewWithTextOrRaise('Select Taskgroup').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('Manual Testing').touch()
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
	vc.findViewWithTextOrRaise('Select Task').touch()
except Exception as e: 
	exception.append(str(e))
try:
	vc.dump(window = -1)
except Exception as e:
	pass

try:
	vc.findViewWithTextOrRaise('Manual').touch()
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

logger().generate_log()

logger().add_test_info(Passed=step_results.count("Passed"), Failed=step_results.count("Failed"))

logger().final_sequence(start_time,step_results,exception_result,time_result)