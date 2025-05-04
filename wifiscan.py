import network
wlan=network.WLAN(network.STA_IF)
wlan.active(True)
accesspoints = wlan.scan()
for ap in accesspoints:
        print(ap)
        
wlan.connect("Galaxy A22 5G9122","ydkq")
print(wlan.isconnected())