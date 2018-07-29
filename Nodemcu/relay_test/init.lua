while(true)
do
	tmr.stop(0);
    print("Turn Off")
	gpio.write(1,gpio.LOW)
	tmr.delay(1000000)
    print("Turn On")
	gpio.write(1,gpio.HIGH)
	tmr.delay(1000000)
end
