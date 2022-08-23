DHT22 / AM2302 Digital Humidity and Temperature Sensor Module
plugged into rasp pi 4<br>

PI prep work after fresh rasp os <br>
<br>
as root<br>
apt install python3-pip<br>
<br>
as user<br>
\curl -sSL https://get.initialstate.com/python -o - | sudo bash <br>
pip3 install adafruit-circuitpython-dht <br>
sudo apt-get install libgpiod2 <br>

<br>
my config :<br>
on sensor<br>

vcc ~ white cable ~ 5v pin2<br>
data ~ red cable ~ pin 7 (gpio 4)<br>
grd ~ blue cable ~ pin 6 (on pi4 ran to pin 9)<br>

<br>
schematic<br>
![PI Diagram](R-Pi-4-GPIO-Pinout-1-768x572.webp)