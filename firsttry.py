import threading


class santhosh():
    def __init__(self,color,john):
        self.color = color
        self.john = john
    def run(self):
        for i in range(50):
            if (i%2==0):
                print(self.color)
            else:
                print(self.john)


    def runed(self):
        print("==================================")
        print(self.john)
        print(self.color)
    
p = santhosh("san","sandy")
i=0
threads = 32
while i<=threads:
    if i%2 == 0:

        t = threading.Thread(target=p.run(),args=(p,) )
        t.start()
    else:
        t = threading.Thread(target=p.runed(),args=(p,) )
        t.start()
    i += 1     

johnny = p.color

print(johnny)