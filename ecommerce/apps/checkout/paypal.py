import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "ATtpK5tu7AKr98Mbdk7mVgxkq0hbSVSTw6NUIjiXu7EpOKj5ySfaQMDgu_c1GxSLVe3XISrcSUrAkGNc"
        self.client_secret = "EPT04Z8FP75Si2zozpvlt50QNwSSQAQkNrGr58XW6Y_al0PFILF6x0xTRWTI9d31gpOZKH_WjfH01_0G"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
