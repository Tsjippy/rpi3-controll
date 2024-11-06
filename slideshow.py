print("Slideshow off")
os.popen("kill $(ps -efw | grep PictureFrame2020 | grep -v grep | awk '{print $2}')")

message = "Slideshow is turned off."

print("Slideshow on")
result=os.system('DISPLAY=:0.0 python3 /home/pi/pi3d_demos/PictureFrame2020.py -m False --show_text "date location" &')
print(result)
message = "Slideshow is turned on."