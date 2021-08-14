
# Simple Password Bruteforcer with only numeric input
# using a python generator

import time

def bruteforce_pw() -> str:
    pwd = 0
    while True:
        yield str(pwd)
        pwd+=1

class Application:

    def testbed(self):
        return ('John Doe', '8923311')        

    def login(self, passwd, passwd2):
        return passwd == passwd2

    def simulate(self):
        ms_start = time.time()
        print("Starting".ljust(80, '.'), str(ms_start-ms_start))
        username, password = self.testbed()
        pw_gen = bruteforce_pw()
        while True:
            nx_pwd = next(pw_gen)
            if self.login(password, nx_pwd):
                break
        ms_end = time.time()
        print(f"Found password {nx_pwd}".ljust(80, '.'), str((ms_end-ms_start)*1000))


if '__main__' == __name__:
    app = Application()
    app.simulate()

    # Output:
    #
    # Starting........................................................................ 0.0
    # Found password 8923311.......................................................... 2890.839099884033