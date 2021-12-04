def losowanie():
    from random import randrange

    lst = ['Antek', 'Bochyn', 'Hadziu', 'Karolina', 'Pieniek', 'Jezus', 'Gorszy', 'Gontarek', 'Jaron', \
            'Staniak', 'Sylwia', 'Tomek', 'Wiktor', "Aleks"]

    newmax: int = 0
    for name in lst:
        if len(name) > newmax:
            newmax = len(name)
            
    for i, name in enumerate(lst):
        if len(name) < newmax:
            name += r"1" * (newmax - len(name))
            lst[i] = name

    copy = lst.copy()

##############################################################################################################

    def convertToBinary(string):
        tobyte = bytearray(string, 'utf8')
        byte_list = []
        
        for byte in tobyte:
            byte_list.append(bin(byte)[2:])
        
        return ' '.join(byte_list)
    

    import signal
    class timeout:
        def __init__(self, seconds=1, error_message='Timeout'):
            self.seconds = seconds
            self.error_message = error_message
        def handle_timeout(self, signum, frame):
            raise TimeoutError(self.error_message)
        def __enter__(self):
            signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.alarm(self.seconds)
        def __exit__(self, type, value, traceback):
            signal.alarm(0)

##############################################################################################################

    wynik = {}
    done = False
    while not done:
        try:
            with timeout(seconds=1):
                for x in lst:
                    index = randrange(len(copy))
                    while x == copy[index]: index = randrange(len(copy))
                    wynik[x] = copy.pop(index)
            done = True
        except:
            break
        
    for x in wynik:
        if x == wynik[x]:
            print(f"!!!zle!!! ---{x} : {wynik[x]}")
            
    if __name__ != '__main__':
        koncowy = {}
        for x in wynik:
            koncowy[x.replace("1", "")] = wynik[x].replace("1", "")
        return koncowy
    else:
        for x in wynik:
            print(f"{x} -> {convertToBinary(wynik[x])}")
            
if __name__ == "__main__":
    losowanie()