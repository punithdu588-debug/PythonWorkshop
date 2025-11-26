class Vehicle:

    def __init__(self):
        pass

    def callings(self):
        print('Invoking Calling Function')

    def sms(self):
        print("Invoking SMS Method")

    def games(self):
        print("Invoking Games")


class Vivot4(Vehicle):

    def cam(self):
        print("Invoking can Method")

    def music(self):
        print("Invoking Music method")

    def video_call(self):
        print("Invoking a video call method")



vivo=Vivot4()
vivo.cam()
vivo.video_call()

