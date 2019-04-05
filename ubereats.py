import socket

def send_client(data):
    host_client='192.168.0.108'
    port_client=21

    s_client=socket.socket()
    s_client.connect((host_client,port_client))
    print('connection done with client')

    s_client.send(data.encode('utf-8'))
    print('msg sent to client')
    s_client.close()

def Main():
    host_avaya = '192.168.0.109'
    port_avaya = 5000

    s_avaya = socket.socket()  #socket for avaya
    s_avaya.bind((host_avaya,port_avaya))    #binding socket
    print('binding complete')
    s_avaya.listen(2)
    print('listening')
    avaya, addr = s_avaya.accept()
    print(addr)
    print(type(addr))
    print("Connection from: " + str(addr))
    while True:
        data = avaya.recv(1024).decode('utf-8')    #receiving from avaya
        if data:
            #data=avaya_chatbot(data)
            print("from connected user: " + data)
            data = data.upper()
            print("sending: " + data)
            #send_ubereats(data)
            #client.send(data.encode('utf-8'))       #sending client
            break
    avaya.close()                          #closing connection

    send_client(data+" ubereats")

if __name__ == '__main__':
    Main()
