import rotatescreen as rs
import time
screen = rs.get_primary_display()
i=0
time.sleep(3)
while i<10000:
	screen.rotate_to((90*i)%360)
	i+=1
#	time.sleep(1)
