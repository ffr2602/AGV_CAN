# Program Kontrol PID ROBOT
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class PID:

    # Variabel Error PID
    i_err = 0
    d_err = 0
    last_err = 0
    
    # Variabel Kp, Ki, Kd 
    def __init__(self, kp=0, ki=0, kd=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    # Compute PID 
    def compute(self, error, limit) -> float:
        self.d_err = error - self.last_err
        self.i_err += error
        self.last_err = error
        result_pid = (self.kp * error) + (self.ki * self.i_err) + (self.kd * self.d_err)
        if result_pid >= 0:
            return limit if result_pid > limit else result_pid
        else:
            return -limit if result_pid < -limit else result_pid
        
    # Reset Error PID
    def reset_err(self):
        self.i_err = 0
        self.d_err = 0
        self.last_err = 0