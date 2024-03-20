# Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the same timestamp.

class Logger:
    def __init__(self):
        self.history = {}  # stores past messages in the form {message: last print timestamp}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.history and timestamp - self.history[message] < 10:  # O(1)
            return False
        else:
            self.history[message] = timestamp  # O(1)
            return True
        return False
        
logger = Logger();
print (logger.shouldPrintMessage(1, "foo"));  # return true, next allowed timestamp for "foo" is 1 + 10 = 11
print (logger.shouldPrintMessage(2, "bar"));  # return true, next allowed timestamp for "bar" is 2 + 10 = 12
print (logger.shouldPrintMessage(3, "foo"));  # 3 < 11, return false
print (logger.shouldPrintMessage(8, "bar"));  # 8 < 12, return false
print (logger.shouldPrintMessage(10, "foo")); # 10 < 11, return false
print (logger.shouldPrintMessage(11, "foo")); # 11 >= 11, return true 