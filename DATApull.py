import serial
import datetime

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
st = ""
y = 0

while True:
    read_serial=ser.readline()
    s[0] = str(str (ser.readline()))
   # print s[0]
    #find and cut gprmc
    st = s[0].split("$GPRMC,",1)
    #print st[1]
    st = st[1]
    st = st.split(',')

     
    x = 0
    while x<13:
        print st[x]
        x = x+1
    latitude = 0;
    latitude = float(st[2][:-7])
    latitude = latitude + (float(st[2][-7:]) / 60)
    if st[3] != "N":
        latitude = latitude*-1

    longitude = 0;
    longitude = float(st[4][:-7])
    longitude = longitude + (float(st[4][-7:]) / 60)
    
    if st[5] != "E":
        longitude = longitude*-1

    temperature = st[12][:-2]
    
    print latitude
    print longitude
    print "Cesius: " + temperature 
    # print read_serial

   
    
    if y < 1000:
        lat = str(latitude)
        lon = str(longitude)
        data_file = open('datafile.txt', 'a')
        data_file.write(str(datetime.datetime.now()))
        data_file.write("\n")
        data_file.write(lat)
        data_file.write("\n")
        data_file.write(lon)
        data_file.write("\n")
        data_file.write(temperature)
        data_file.write("\n")
        data_file.close()
        y = y+1
    else:
        data_file = open('datafile.txt', 'w')
        data_file.close()
        print("File overwritten")
        y = 0
    
   
        
         
        
        
        
    

    


