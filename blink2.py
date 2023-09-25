from machine import Pin, Timer
led1 = Pin(26, Pin.OUT)
led2 = Pin(22, Pin.OUT)
led3 = Pin(21, Pin.OUT)
led4 = Pin(20, Pin.OUT)
led5 = Pin(19, Pin.OUT)
led6 = Pin(18, Pin.OUT)
led7 = Pin(17, Pin.OUT)
led8 = Pin(16, Pin.OUT)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
led7.value(0)
led8.value(0)

timer = Timer()
counter = 0

def blink(timer):
    global counter
    counter += 1;
    
    #1
    led1.toggle()
    #2
    if counter%2 == 0:
        led2.toggle()
    #3
    if counter%4 == 0:
        led3.toggle()
    #4
    if counter%8 == 0:
        led4.toggle()
    #5
    if counter%16 == 0:
        led5.toggle()
    #6
    if counter%32 ==0:
        led6.toggle()
    #7
    if counter%64 == 0:
        led7.toggle()
    #8
    if counter%128 ==0:
        led8.toggle()
     
    print("LOOP!")

    
timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)