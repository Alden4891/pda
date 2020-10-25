------------------------------------------------------------------------------------------------
# SAMPPLE SEND COMMAND WITH CC AND BCC 
toaddr = 'buffy@sunnydale.k12.ca.us'
cc = ['alexander@sunydale.k12.ca.us','willow@sunnydale.k12.ca.us']
bcc = ['chairman@slayerscouncil.uk']
fromaddr = 'giles@sunnydale.k12.ca.us'
message_subject = "disturbance in sector 7"
message_text = "Three are dead in an attack in the sewers below sector 7."
message = "From: %s\r\n" % fromaddr
        + "To: %s\r\n" % toaddr
        + "CC: %s\r\n" % ",".join(cc)
        + "Subject: %s\r\n" % message_subject
        + "\r\n" 
        + message_text
toaddrs = [toaddr] + cc + bcc
server = smtplib.SMTP('smtp.sunnydale.k12.ca.us')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, message)
server.quit()
------------------------------------------------------------------------------------------------
# ACCOUNT IS BLOCKED BY THE MAIL SERVER
Hi Danielle, the python connection needs to be authenticated.  By the look of that error message you have two step verification enabled on the account so you need to create an Application Specific Password nd use that in your python code.  See Signing in using application-specific passwords

If I'm wrong and you do not have 2SV enabled, then you must enable access for less secure apps: sign into the Gmail account using a web browser at https://mail.google.com, then go to Settings > Accounts and Import > Other Google Account settings.  Under Security, scroll down and enable access for less secure apps. This setting is required to enable SMTP, POP or IMAP access.

If it still fails, you might need to clear Captcha: visit https://accounts.google.com/DisplayUnlockCaptcha and sign in with the Gmail username and password.  If necessary (it's usually not), enter the letters in the distorted picture then press Continue. This will allow ten minutes for the python code to register as an approved connection.  Note that you must use the account you are using in your code - if the browser is already signed into another account, you must sign out first. Also, you must trigger the code to make a connection within ten minutes of pressing Continue.