class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.did=[]
        self.undid=[]

    def add(self, num: int):
        self.value += num
        self.did.append([1,num])
        #self.undid = [] ok so this is not needed wtf... change does not clear cache of undo


    def subtract(self, num: int):
        self.value -= num
        self.did.append([0,num])
        #self.undid = [] ok so this is not needed wtf...

    def undo(self):
        if(len(self.did)):
            change = self.did[-1]
            self.did.pop()
            op = change[0]
            num = change[1]
            if(op == 0): # subtract so we add
                self.value += num
            else:
                self.value -= num
            self.undid.append(change)


    def redo(self):
        if(len(self.undid)):
             change = self.undid[-1]
             self.undid.pop()
             op = change [0]
             num = change [1]
             if(op == 1): # add so add
                self.value += num
             else:
                self.value -= num
             self.did.append(change)

    def bulk_undo(self, steps: int):
        for i in range (0, steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range (0, steps):
            self.redo()
