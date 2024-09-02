Smart Security Camera with Motion Detection

This project is a Python-based security camera application that uses OpenCV and Tkinter to provide a simple graphical user interface (GUI) and automated motion detection. The camera can detect faces and bodies, automatically start recording when motion is detected, and stop recording after a specified period of inactivity.

Features:
Live Video Stream: The application streams live video from the camera, displayed in a user-friendly GUI.
Motion Detection: Utilizes OpenCV's Haar cascades to detect faces and bodies in the video feed.
Automated Recording: Starts recording automatically when motion is detected and continues for a few seconds after motion stops.
Configurable Delay: The recording continues for a customizable period (default is 5 seconds) after the last detected motion to ensure no crucial moments are missed.
Simple GUI: Built with Tkinter, the interface includes buttons to start the video feed and exit the application.
Video Storage: Recorded videos are saved in MP4 format with timestamps in the filename.
