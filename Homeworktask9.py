import datetime

class Logger:
    def __init__(self, log_path):
        self.log_file = open(log_path, 'w')

    def __enter__(self):
        return (self)

    def write_log(self, action):
        self.log_file.write(f'{datetime.datetime.utcnow()}: {action} \n ')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_log(f'error: {exc_val}')
        t3 = datetime.datetime.utcnow()
        self.write_log(f'Time of end of program. The length of the program in time is {t2-t1}\n The difference of time between the end of working cycle and writing this note about the end of the program - {t3-t2}')
        self.log_file.close()

if __name__== '__main__':
    with Logger ('my.log') as log:
        t1=datetime.datetime.utcnow()
        print (t1)
        log.write_log('Time of beginning of program')
        a=2+2
        b=a**10000
        print(b**100 - a) #only thing I could imagine when there is some time required for process.
        #all the homeworks weren't long enought to count a time
        t2 = datetime.datetime.utcnow()
        log.write_log(f'The time of executing the code, which is executing in the context manager-{t2-t1}')