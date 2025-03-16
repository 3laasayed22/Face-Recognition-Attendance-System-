import os
import time
import datetime
import yagmail
while True :
    ts = int(time.time())
    time2 = str(datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S'))
    print(time2,"time")
    if time2 == '14:04:30':

        receiver = ""  # receiver email address
        body = "Attendence File"  # email body
        filename = "Attendance"+os.sep+"Attendance.csv"  # attach the file

        # mail information
        yag = yagmail.SMTP("","")

        # sent the mail
        yag.send(
                    to=receiver,
                    subject="Hex Attendance Report",  # email subject
                    contents=body,  # email body
                    attachments=filename,  # file attached
                            )
