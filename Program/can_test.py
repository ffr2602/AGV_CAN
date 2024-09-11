import can 
from can.interfaces.serial.serial_can import SerialBus as Bus

CAN_ID_first_set = [0x301, 0x302]
CAN_ID = [0x501, 0x502]

CAN_ID_sensor = 0x186

class CAN_setting():
    def __init__(self) -> None:
        self.can_open = False

        # Check CAN Communication
        try:
            # self.bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=500000)
            self.bus = Bus(bau)
            self.can_open = True
        except OSError:
            self.can_open = False
            exit()
        
        # Send Initialize Motor
        if self.can_open == True:
            self.bus.send(can.Message(arbitration_id=0x000, data=[0x01,0x00]))
            for i in range(len(CAN_ID_first_set)):
                self.bus.send(can.Message(arbitration_id=CAN_ID_first_set[i], data=[0x0f,0x00,0x00,0x00,0x00,0x00]))

    def set_kecepatan_motor(self, speed):
        if self.can_open == True:
            for i in range(len(speed)):
                self.bus.send(can.Message(arbitration_id=CAN_ID[i], data=[0x0f,0x00,
                                                                          int(hex(speed[i] & 0xff), 16),
                                                                          int(hex(speed[i] >> 8 & 0xff), 16),
                                                                          int(hex(speed[i] >> 16 & 0xff), 16),
                                                                          int(hex(speed[i] >> 32 & 0xff), 16),0x00,0x00]))
                
    def read_data_sensor(self):
        if self.can_open == True:
            msg_recv = self.bus.recv()
            print(msg_recv)
            # if hex(msg_recv.arbitration_id) == hex(CAN_ID_sensor):
            #     a = msg_recv.data[msg_recv.dlc - 6]
            #     b = msg_recv.data[msg_recv.dlc - 5] * 0x100
            #     c = msg_recv.data[msg_recv.dlc - 4] * 0x10000
            #     d = msg_recv.data[msg_recv.dlc - 3] * 0x1000000
            


    def monitor_data(self):
        mesg = self.bus.recv()
        print(mesg)



if __name__ == '__main__':
    app = CAN_setting()
    while True:
        app.read_data_sensor()

