def getcommand(text):
    import speech_recognition as sr
    import os
    import dbus
    import requests
    import gtts
    import time
    from playsound import playsound

    # initalize dbus for spotify, recognizer, microphone
    #r=sr.Recognizer()
    #mic=sr.Microphone(device_index=0)
    bus = dbus.SessionBus()
    proxy = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    interface = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
	
    # play listening sound 
    #playsound('./listening.wav')
    #r.adjust_for_ambient_noise(sr.Microphone(device_index=0))
    #print('speak')
	
    # Record audio from the microphone we initialized earlier
#    with mic as source:
    playsound('/home/ryals/Documents/ryals-pc-assistant/listening.wav')    
#   ┌───────┐
#   │PROGRAM│ 
#   └───────┘
    if 'open Google' in text:
        os.system('google-chrome')
    if 'open Terminal' in text:
        os.system('terminator')
    if 'open word' in text:
        os.system('libreoffice')
	    
    #   ┌───────┐
    #   │NETWORK│
    #   └───────┘
    if 'synchronize one drive' in text:
        os.system('onedrive --synchronize')
    if 'what is my public address' in text:
        ip = requests.get('http://www.loopware.com/ip.php')
        gTTS(ip)
    #   ┌───────┐
    #   │SPOTIFY│ 
    #   └───────┘
    if 'open music' in text:
        os.system('spotify >/dev/null')
    if 'pause music' in text:
        interface.Pause()
    if 'play music' in text:
        interface.Play()
    if 'skip' in text:
        interface.Next()
    if 'rewind' in text:
        interface.Previous()
    
    #   
    #
    #
