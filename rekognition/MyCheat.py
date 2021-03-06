import threading
import Queue

def parseWaste(key):
    if(key == '1'):
        return 'UNSORTED'
    elif(key == '2'):
        return 'PLASTIC'
    elif(key == '3'):
        return 'PAPER'
    elif(key == '4'):
        return 'GLASS'
    elif(key == '5'):
        return 'EMPTY'
    else:
        return 'UNSORTED'


class MyCheat(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.is_running = True
       
    def run(self):
        while(self.is_running):
            waste = raw_input('')
            waste = parseWaste(waste)
            if not self.queue.full():
                self.queue.put(waste)

    def stop(self):
        self.is_running = False