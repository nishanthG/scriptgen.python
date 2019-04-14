from ScreenShot import Screenshot
from Screen_Shot_Button import startGUI
from AQMdroid import AQMdroid
from SciptMaker import ScriptMaker

def main():
	ScriptMaker().create_files()
	ScriptMaker().write_initial_content()
	startGUI().run()

if __name__ == '__main__':
 	main() 

 	