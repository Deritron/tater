#Wijziging op GitHub - Nieuw
import time
import datetime
import RPi.GPIO as GPIO

#initialisatie pinnetje
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #we gebruiken de fysieke pin nummer(pinout)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) #bijopstarten staat pinnetje altijd af


#watertijd is de duurtijd in seconde dat hij water zal geven
watertijd = 4



#beginnen met water geven
print ("Ik begin nu met water te geven voor:", watertijd, " seconden.")

logbestand=open("/webapp/taterlog.txt","a+")
nu=datetime.datetime.now()
huidigetijd = str(nu)
print(huidigetijd)
logbestand.write(huidigetijd)
logbestand.write("\r\n Ik begin nu water te geven \r\n")

GPIO.output(8, GPIO.HIGH)

#start timer
time.sleep(watertijd)

GPIO.output(8, GPIO.LOW)
print ("Ik ben nu klaar met water geven.")

#logbestand=open("/webapp/taterlog.txt","a+")
nu=datetime.datetime.now()
huidigetijd = str(nu)
print(huidigetijd)
logbestand.write(huidigetijd)
logbestand.write("\r\n Ik ben klaar met water geven \r\n")
logbestand.write("***************************************** \r\n")

