import socket
import serial

Arduino = serial.Serial('/dev/ttyACM0', 9600)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
server.bind((host, 8089))
server.listen(5)

while True:
 
    conn, addr = server.accept()
    cmnd = conn.recv(1) 
    print(cmnd)


    if 'A' in str(cmnd):
        conn.sendall(b'RECIBIDO-A')
        Arduino.write(('A').encode())
        
    elif 'B' in str(cmnd):
        conn.sendall(b'RECIBIDO-B')
        Arduino.write(('B').encode())  

    elif 'C' in str(cmnd):
        conn.sendall(b'RECIBIDO-C')
        Arduino.write(('C').encode())
        
    elif 'D' in str(cmnd):
        conn.sendall(b'RECIBIDO-D')
        Arduino.write(('D').encode())

    elif 'E' in str(cmnd):
        conn.sendall(b'RECIBIDO-E')
        Arduino.write(('E').encode())

    elif 'F' in str(cmnd):
        conn.sendall(b'RECIBIDO-F')
        Arduino.write(('F').encode())

    elif 'G' in str(cmnd):
        conn.sendall(b'RECIBIDO-G')
        Arduino.write(('G').encode())

    elif 'H' in str(cmnd):
        conn.sendall(b'RECIBIDO-H')
        Arduino.write(('H').encode())

    elif 'I' in str(cmnd):
        conn.sendall(b'RECIBIDO-I')
        Arduino.write(('I').encode())

    elif 'J' in str(cmnd):
        conn.sendall(b'RECIBIDO-J')
        Arduino.write(('J').encode())

    elif 'S' in str(cmnd):
        conn.sendall(b'RECIBIDO-S')
        Arduino.write(('S').encode())

    #elif 'V' in str(cmnd):
    #    conn.sendall(b'RECIBIDO-V')
    #    Arduino.write(("V").encode())

    #elif 'X' in str(cmnd):
    #    conn.sendall(b'RECIBIDO-X')
    #    Arduino.write(("X").encode())

    #elif 'Y' in str(cmnd):
    #    conn.sendall(b'RECIBIDO-Y')
    #    Arduino.write(("Y").encode())

    #elif 'Z' in str(cmnd):
    #    conn.sendall(b'RECIBIDO-Z')
    #    Arduino.write(("Z").encode())

    #----------------------------------------------


server.close()
