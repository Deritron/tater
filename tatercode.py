#test lijntje erbij via GitHub website
import time
import datetime
import RPi.GPIO as GPIO

#initialisatie pinnetje
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #we gebruiken de fysieke pin nummer in de plaats van de GPIO nummer. (zie commando "pinout" op de Raspberry Pi
GPIO.setup(3, GPIO.OUT) #bijopstarten staat pinnetje altijd af


#watertijd is de duurtijd in seconde dat hij water zal geven
watertijd = 120



#beginnen met water geven
print ("Ik begin nu met water te geven voor:", watertijd, " seconden.")

logbestand=open("/webapp/taterlog.txt","a+")
nu=datetime.datetime.now()
huidigetijd = str(nu)
print(huidigetijd)
logbestand.write(huidigetijd)
logbestand.write("\r\nIk begin nu water te geven.\r\n")

GPIO.output(3, GPIO.LOW)

#start timer
time.sleep(watertijd)

GPIO.output(3, GPIO.HIGH)
print ("Ik ben nu klaar met water geven.")


#logbestand=open("/webapp/taterlog.txt","a+")
nu=datetime.datetime.now()
huidigetijd = str(nu)
print(huidigetijd)
logbestand.write(huidigetijd)
logbestand.write("\r\nIk ben klaar met water geven.\r\n")
logbestand.write("*****************************************\r\n")

