@echo off
cls
echo Conecte su placa, asegurese de que es detectada
echo si no se detecta instale el driver CH340 de esta carpeta
echo:
set /p NUM=COM: 
set /p PLACA=esp:

echo su puerto es COM%NUM% y su placa es la esp%PLACA%

set /p OK=Es correcto (Y, N): 
if %OK%==Y GOTO CONFIG
if %OK%==y GOTO CONFIG
GOTO FAIL

:CONFIG
if %PLACA%==8266 GOTO ESP8266
if %PLACA%==32 GOTO ESP32
echo no se ha seleccionado una placa valida
GOTO FAIL

:ESP8266
echo Configurando ESP-8266
cd config
python esptool/esptool.py --port COM%NUM% erase_flash
::--baud 115200
python esptool/esptool.py --port COM%NUM% --baud 460800 write_flash --flash_size=detect 0 micropython/esp8266-20220618-v1.19.1.bin
GOTO END

:ESP32
echo Configurando ESP-32
cd config
python esptool/esptool.py --port COM%NUM% erase_flash
::--baud 115200 
python esptool/esptool.py --chip esp32 --port COM%NUM% --baud 460800 write_flash -z 0x1000 micropython/esp32-20220618-v1.19.1.bin
GOTO END

:END
echo Se ha configurado correctamente
pause
exit

:FAIL
echo Se a cancelado la configuracion
pause
exit