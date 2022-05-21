import urllib.request
import time
from PIL import Image
import os
import sys
import subprocess

def msg(txt):
    sys.stdout.write(txt)
    sys.stdout.flush()
try:
	start_time = time.time()
	scan = False
	argc = len(sys.argv) -1
	argv = sys.argv
	cmd = """osascript -e 'tell application "Finder"
	 activate
	 display alert "Download successful!"
	end tell'"""
	def searchArg(argchar, numberArg, argument):
			output = "ERROR"
			if numberArg >= 3:
				i = 0
				while i <= numberArg:
					if str(argchar[i]) == argument:
						output = argchar[i+1]     
						break;
					i = i + 1
			return output;
	if argc >= 5:
		nameScan = searchArg(argv, argc, "-n")
		url_site = searchArg(argv, argc, "-u")
		tome = searchArg(argv, argc, "-t")
		firstChap = searchArg(argv, argc, "-f")
		lastChap = searchArg(argv, argc, "-l")
		format = searchArg(argv, argc, "-z")
		if nameScan and url_site and tome and firstChap and lastChap != "ERROR":

				opener = urllib.request.build_opener()
				opener.addheaders = [('User-agent', 'Mozilla/5.0')]
				urllib.request.install_opener(opener)
				name=[]
				nameScan= str(nameScan)
				url_site = str(url_site)
				tome = str(tome)
				firstChap = int(firstChap)
				lastChap = int(lastChap)

				path = str(nameScan)+str(tome)

				# Check whether the specified path exists or not
				isExist = os.path.exists(path)

				if not isExist:
				  
				  # Create a new directory because it does not exist 
				  os.makedirs(path)
				format = str(format)
				for i in range(firstChap, lastChap+1):
					if format == "odd":
						if len(str(i))==1:
							urllib.request.urlretrieve(str(url_site) + "00"+ str(i)+".jpg", str(nameScan)+str(tome)+"/"+str(nameScan)+str(i)+".jpg")
						elif len(str(i))==2:
							urllib.request.urlretrieve(str(url_site) +  "0"+str(i)+".jpg", str(nameScan)+str(tome)+"/"+str(nameScan)+str(i)+".jpg")
						else:
							urllib.request.urlretrieve(str(url_site) + str(i)+".jpg", str(nameScan)+str(tome)+"/"+str(nameScan)+str(i)+".jpg")
					else:
						urllib.request.urlretrieve(str(url_site) + str(i)+".jpg", str(nameScan)+str(tome)+"/"+str(nameScan)+str(i)+".jpg")
					m = "%d chapter left" % (lastChap-i)
					msg(str(m) + chr(13))	
					name.append(str(nameScan)+str(tome)+"/"+str(nameScan)+str(i)+".jpg")
					
				images = [
				    Image.open(f)
				    for f in name
				]

				pdf_path = str(nameScan)+str(tome)+".pdf"

				images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

				print("\n--- %s seconds ---" % (time.time() - start_time))
				
				scan = True
	else:
	    print ('+' + '-'*32 + '+')
	    print ('|' + ' '*14 + 'HELP' + " "*14 + '|')
	    print ('+' + '-'*32 + '+')
	    print ('Wrong use !\nRight use : \n-u "url" \n-n "name" \n-t "tome" \n-f "first chap" \n-l "last chap \n-z "odd/even"')
	if scan == True:
		if sys.platform == "darwin":
		#os.system(cmd)
			subprocess.check_output(str(cmd), shell=True)
		elif sys.platform == "win32"
			ubprocess.check_output('mshta vbscript:Close(MsgBox("Hello, World!"))', shell=True)
		else:
			print("\nDownload successful!")
	else:
	    quit()
except:
	quit()