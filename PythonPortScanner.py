import socket 
import sys 

def scanner(ip , port ):
    s = socket.socket ( socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip , int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()
if(scanner(sys.argv[1] , sys.argv[2])):
    print(sys.argv[1] + '::OPEN')
else:
    print(sys.argv[1] + '::CLOSE')
