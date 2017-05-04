
from gpiozero import LightSensor, Buzzer

ldr = LightSensor(17)  # alter if using a different pin
ldr.wait_for_light()
#print("Light detected!")
while True:
 print(ldr.value)
