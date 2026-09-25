import time as tm
import machine as m
import ServoMovements as sm
s1 = sm.servo(5)
s2 = sm.servo(19)
see = sm.servo(12)
class initComms:
    global MSG
    def __init__(self):
        m.Pin(2, m.Pin.OUT).off()
        import network as intnet
        import socket
        net = intnet.WLAN(intnet.STA_IF)
        net.active(1)
        net.connect("SSID", "password") #Enter the SSID and password of the WiFi connection you intend to use. You may also start a WiFi connection from your microcontroller.
        print(net.status())
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net.ifconfig(["configure your IP adress settings as required"])
        print(net.ifconfig())
        self.s.bind(("", 80))
        self.s.listen(1)
        
        while True:
            m.Pin(2, m.Pin.OUT).on()
            tm.sleep(0.5)
            m.Pin(2, m.Pin.OUT).off()
            client, addr = self.s.accept()
            m.Pin(2, m.Pin.OUT).on()
            tm.sleep(0.5)
            m.Pin(2, m.Pin.OUT).off()
            tm.sleep(2)
            while True:
                msg = client.recv(1024).decode('utf-8')
                print(msg)
                command = msg.split(",")
                if command[0] == "up":
                    s2.rotate(float(command[1]))
                    client.send(bytes("command complied with", "utf-8"))
                elif command[0] == "down":
                    s1.rotate(float(command[1]))
                    client.send(bytes("command complied with", "utf-8"))
                elif command[0] == "End Effector":
                    if command[1] == "release":
                        see.rotate(0)
                    elif command[1] == "engage":
                        see.rotate(135)
                else:
                    client.send(bytes("Improper command send", "utf-8"))
