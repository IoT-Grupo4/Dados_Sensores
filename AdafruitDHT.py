#!/usr/bin/python
# Author: Larinni Malheiros


import sys
import time
import Adafruit_DHT
import csv

file = open('file.csv', 'w')
wr = csv.writer(file, quoting=csv.QUOTE_ALL)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Lendo de um  AM2302 conectado ao GPIO')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

print ("*** Lendo os valores de temperatura e umidade");

while True:
	if humidity is not None and temperature is not None:
    		print('Temperatura={0:0.1f}*  Humidade={1:0.1f}%'.format(temperature, humidity))
		wr.writerow([temperature, humidity])
		print ("Aguarda 3 segundos para efetuar nova leitura...\n");
     		time.sleep(3)
	else:
    		print('Falha ao ler dados do DHT11. Tente Novamente!')
    		sys.exit(1)
