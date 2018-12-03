# camerasort
test repo for camera sorting
To access camera, use Internet Explorer, install plugin.  Page should login with username/password

Set up FTP scheduled snaps, file format is Schedule_yyyymmdd-hhmmss.jpg

Use this command on directory with .jpg files to turn them all into a timelapse image.  Speed of video can be changed by changing FTP snap interval or framerate of finished video.  our scripts use 50fps to limit overall time.

ffmpeg -framerate 25 -pattern_type glob -i "*.jpg" -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4

Static image updating every 30 seconds
Linked from GODO page

Timelapse: Event based
Divide images by days, Dave will supply dates for major construction events

November 7

#Instructions on how to do this thing:
#Set up Foscam to upload snapshots to mhstorage1 via FTP
#cron job on mhstorage1, a script called sort.py that automatically puts snapshots into day folders, every 5 minutes.
#cron job on lo-gateway, shell script that pushes some files to lowell.edu, overwriting current image on godo_live.php
#scripts here that will go into every directory, and attempt to create a 50fps timelapse with all jpgs in the directory called quicksort.sh and quickmp4.sh.  quicksort.sh deletes all images before 7:00AM and after 6:00PM (night time)
#then we build mylist.txt.  There's probably a smarter way to do this but I just made a spreadsheet and copy-pasted
#
#command that creates a concatenated timelapse:
#ffmpeg -f concat -i mylist.txt -c copy output1.mp4
