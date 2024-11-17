import network


def connection():
    import network
    ssid = 'LIMITED2'
    password = '123.ILUV'

    #wlan.active(False)
    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print('Connecting...')
    print('network config:', wlan.ifconfig())

connection()