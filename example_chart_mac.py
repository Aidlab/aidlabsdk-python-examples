from Aidlab.Aidlab import Aidlab
from Aidlab.Plot import Plot


class MainManager(Aidlab):

    def __init__(self):
        super().__init__()
        self.plot = Plot()

    def did_connect_aidlab(self, aidlab_address):
        print("Connected to: ", aidlab_address)

    def did_disconnect_aidlab(self, aidlab_address):
        print("Disconnected from: ", aidlab_address)

    def did_receive_ecg(self, value, timestamp, aidlab_address):
        self.plot.add(value)


if __name__ == '__main__':

    characteristics = ["ecg"]

    main_manager = MainManager()
    main_manager.connect(characteristics)

    while True:
        pass