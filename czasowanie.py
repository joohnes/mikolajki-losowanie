def plotowanie(amount):
    from matplotlib.pyplot import plot
    from prezenty import losowanie
    from time import perf_counter, localtime
    import matplotlib.pyplot as plt
    from mail import sendMail

    def getDivider(num: int) -> int:
        # divider = [(id, x) for id, x in enumerate(str(num)) if x not in ["0", "."]]
        # return int(divider[0][1]) * 10 ** -(divider[0][0] + 1)
        return num/100


    lst = ['Antek', 'Bochyn', 'Hadziu', 'Karolina', 'Pieniek', 'Jezus', 'Gorszy', 'Gontarek', 'Jaron', \
            'Staniak', 'Sylwia', 'Tomek', 'Wiktor', "Aleks"]

    wyniki = {}
    for x in lst:
        temp = {}
        for y in lst:
            if x == y: continue
            temp[y] = 0
        wyniki[x] = temp
        
    start_time = f"{localtime().tm_hour:02d}:{localtime().tm_min:02d}:{localtime().tm_sec:02d}"
    czas = perf_counter()
    for _ in range(amount):
        wynik = losowanie()
        for x in wynik:
            wyniki[x][wynik[x]] += 1
            
    czas = perf_counter() - czas    
    temp = int(czas / 3600)
    temp1 = int((czas - temp*3600) / 60)
    temp2 = czas - temp * 3600 - temp1 * 60
    czas = f"{f'{temp:02d}:' if temp > 0 else ''}{f'{temp1:02d}:' if temp1 > 0 else ''}{temp2:.02f}"
    
    occurences = []
    for x in wyniki:
        for y in wyniki[y]:
            if x == y: continue
            occurences.append([wyniki[x][y],f"{x}-{y}"])
            
    occurences = sorted(occurences, reverse=True)

    plt.figure(figsize=(9,5))
    plt.bar([x[1] for x in occurences[:5]], [x[0] for x in occurences[:5]])
    for index, x in enumerate(occurences[:5]):
        plt.text(index, y = x[0] + getDivider(x[0]), s= f"{x[0]} | {(x[0]/amount*100):.2f}%")
    plt.tight_layout()
    plt.savefig('results.png')
    
    predictions = {}
    for name in lst:
        for x in occurences:
            if name == x[1].split('-')[0]:
                try:
                    if x[1].split('-')[1] in [predictions[x][0] for x in predictions]: continue
                    if x[0] > predictions[name][1]:
                        predictions[name] = [x[1].split('-')[1], x[0]]
                except:
                    predictions[name] = [x[1].split('-')[1], x[0]]
  
    
    content = "Predictions:\n"
    left = [x for x in predictions]
    for x in predictions:
        maxnumber = x
        for y in left:
            if predictions[y][1] > predictions[x][1]:
                maxnumber = y
        left.remove(maxnumber)
        content += f"{maxnumber} - {predictions[maxnumber][0]} -- {(predictions[maxnumber][1]/amount * 100):.2f}%\n" 
    for x in predictions:
        content += f"{x} - {predictions[x][0]} - {(predictions[x][1]/amount * 100):.2f}%\n"
    content += '\n\n'
    for x in occurences:
        content += f"{x[1]} - {x[0]} -- {(x[0]/amount * 100):.2f}%\n"
        
    sendMail(Subject=f"Done in {czas}s, started at {start_time}", content=content, file= "results.png")

if __name__ == '__main__':
    AMOUNT = 50000
    
    plotowanie(AMOUNT)
