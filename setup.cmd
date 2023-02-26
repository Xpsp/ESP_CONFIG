mkdir config
cd config
git clone https://github.com/espressif/esptool
curl -O http://lastminuteengineers.b-cdn.net/wp-content/uploads/iot/ESP32-Pinout.png
curl -O http://sparks.gogo.co.nz/assets/_site_/downloads/CH34x_Install_Windows_v3_4.zip
mkdir micropython
cd micropython
curl -O http://micropython.org/resources/firmware/esp8266-20220618-v1.19.1.bin
curl -O http://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin
cd ../..