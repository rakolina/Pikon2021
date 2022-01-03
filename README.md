# Pikon2021
Pikon shutter button and remote preview stream server 

clone this repo into your raspberry pi home folder

Momentary button script needs to reside in /home/pi/Pikon2021 folder

One line has to be added to the /etc/rc.local file (sudo required)

To configure static IP on the Pi we need to edit dhcpcd.conf file and wpa suppilcant file

Web UI to configure the pi camera options resides in default lighttpd directory: /var/www/html


The libcamera stack introduction to Raspberry Pi calls for a clean split between libcamera and legacy support in our project.

https://www.raspberrypi.com/documentation/accessories/camera.html

# Pikon V2
Bullseye based with libcamera stack will use the HD camera.

I. Image formats:
1. JPEG,
2. PEG + DNG (raw), 
3. BMP, 
4. PNG, 
5. YUV420, 
6. RGB888

II. Max exposure (seconds): 230

III. Exposure modes:
1. normal, 
2. short, 
3. long, 
4. fixed fps, 
5. customisable

IV. Video formats
1. raw h.264 (accelerated), 
2. MJPEG

V. Post-processing
User-definable image effects, 
customisable DRC and HDR, 
motion detection, 
OpenCV integration, 
TensorFlowLite integration

VI. Metering modes
1. centre-weighted, 
2. average, 
3. spot, 
4. customisable

VII. Automatic white balance modes
1. off, 
2. auto, 
3. incandescent, 
4. tungsten, 
5. fluorescent, 
6. indoor, 
7. daylight, 
8. cloudy, 
9. customisable

VIII. Triggers
1. Keypress, 
2. UNIX signal, 
3. timeout

IX. Extra modes
1. timelapse, 
2. circular buffer, 
3. motion detection, 
4. segmented video, 
5. many features through flexible post-processing






# Pikon V1
Buster based pikon will use a v2 camera.

I. Available image formats:
JPEG (accelerated), 
1. JPEG + RAW, 
2. GIF, 
3. BMP, 
4. PNG, 
5. YUV420,
6. RGB888

II. Max exposure (seconds): 10

III. Exposure modes:
1. auto, 
2. night, 
3. nightpreview, 
4. backlight, 
5. spotlight, 
6. sports, 
7. snow, 
8. beach, 
9. verylong, 
10. fixedfps, 
11. antishake, 
12. fireworks


Video formats

raw h.264 (accelerated)

Effects

negative,
solarise,
posterize,
whiteboard,
blackboard,
sketch,
denoise,
emboss,
oilpaint,
hatch,
gpen,
pastel,
watercolour,
film,
blur,
saturation


Metering modes

average, spot, backlit, matrix

Automatic white balance modes

off, 
auto, 
sun, 
cloud, 
shade, 
tungsten, 
fluorescent, 
incandescent,
flash, 
horizon

Triggers

Keypress, UNIX signal, timeout

Extra modes

demo, 
burst/timelapse, 
circular buffer, 
video with motion vectors, 
segmented video, 
live preview on 3D models




