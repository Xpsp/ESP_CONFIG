# Para prender el led, conectarse a ESP-AP con pass: 12345678
# escribir la ip que sale, regularmente 192.168.4.1/ledon o /leoff
import network
import socket
from machine import Pin

# Main app
led = Pin(2, Pin.OUT)

def do_command(command):
  if command == 'ledon':
    led.on()
  if command == 'ledoff':
    led.off()

# Wifi - Access Point
SSID = 'ESP-AP'
PASSWORD = '12345678'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, authmode=3, password=PASSWORD)

while ap.active() == False: pass

print('Connection successful')
print(ap.ifconfig()[0])

# Socket
def web_page():
  html = """<html><body><h1>Hello, World!</h1></body></html>"""
  return html

def filter_request(request):
  request = request[5:request.find(b'H')-1]
  return request.decode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr[0]))
  request = conn.recv(1024)
  #print('Content = %s' % str(request)) # debug purposes
  command = filter_request(request)
  do_command(command)
  response = web_page()
  conn.send(response)
  conn.close()