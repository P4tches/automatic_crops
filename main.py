import ota
def start():
    print('wow world')
    
def boot():
    ota.update()
    start()
    
boot()
