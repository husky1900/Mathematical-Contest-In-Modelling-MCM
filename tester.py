track1File = open('track1.txt','r')
track1 = str.split(track1File.readline()[1:-1],',')
print (track1[0])