# try:
#     f=open("e:\\a.txt","r")
#     file=f.readlines()
# except BaseException as msg:
#     print(msg)
# finally:
#     f.close()
#

with open("e:\\a.txt","r") as f:
    print(f.readlines())