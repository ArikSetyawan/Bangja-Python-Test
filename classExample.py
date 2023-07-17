class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("ge A stop")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("go C stop!")

class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("go D stop!")
    def pause(self):
        print("wait D wait!")

d = D()
d.go()