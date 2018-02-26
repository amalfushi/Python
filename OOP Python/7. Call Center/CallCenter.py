class Call(object):
    def __init__(self, idNum, name, phNumber, time, reason):
        self.idNum = idNum
        self.name = name
        self.phNumber = phNumber
        self.time = time
        self.reason = reason

    def display(self):
        print "Call ID#: ", self.idNum
        print "Caller Name: ", self.name
        print "Phone Number: ", self.phNumber
        print "Time of call: ", self.time
        print "Reason for call: ", self.reason


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize = len(self.calls)

    def add(self, call):
        if isinstance(call, list):
            for num in range(0, len(call)):
                self.calls.append(call[num])
        else:
            self.calls.append(call)

        self.queueSize = len(self.calls)
        return self

    def remove(self):
        del calls[0]
        return self

    def remove(self, pNum):
        for call in self.calls:
            if call.phNumber == pNum:
                self.calls.remove(call)

    def info(self):
        for call in self.calls:
            print "{} ({}) --Queue Length: {}".format(call.name, call.phNumber, self.queueSize)
        print ""


    
c1 = Call("991880", "Dustin Schroeder", "(206)555-5554", "14:43", "Girl talk")
c2 = Call("991139", "Sustin Dchroeder", "(206)555-1555", "14:19", "Boy talk")
c3 = Call("999999", "Dr. Frankenstein", "(206)555-5556", "14:55", "uuuuuunnnnnnng")
c4 = Call("992293", "Gandalf", "(206)555-5552", "14:23", "Mordor")
c5 = Call("991000", "Barnaby Jones", "(206)555-2255", "14:03", "Meow")
cCenter1 = CallCenter()

cCenter1.add([c1, c2, c3, c4, c5])
c1.display()

cCenter1.info()
cCenter1.remove("(206)555-1555")
cCenter1.info()