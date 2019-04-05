import socket

def Main():
    host='192.168.0.106'
    port=6000

    s=socket.socket()

    data='order food'
    print('file ot to send')
    s.connect((host,port))
    s.send(data.encode('utf-8'))
    chatbot_ip=s.recv(1024).decode('utf-8')
    print('data recv: ',chatbot_ip)
    print(type(chatbot_ip))
    s.close()

    host = '192.168.0.109'
    port = 5000

    s = socket.socket()
    print('socket done')
    data = 'order food'
    print('file ot to send')
    s.connect((host, port))
    s.send(data.encode('utf-8'))
    result = s.recv(1024).decode('utf-8')
    print('data recv: ', result)
    s.close()



if __name__=='__main__':
    Main()