[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Trade Server](../Trade-Server.md) / SendMail Utility

[Previous](Daily-Reports.md) | [Next](Return-Errors.md)

# SendMail Utility

MetaTrader 5 SendMail is a command-line utility and a component of MetaTrader 5 platform. It is used by a trade server for sending reports and emails. This application can be used for sending reports manually.

## Report Generation

The trade server [prepares reports on (#end-of-day)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#end-of-day) client deals at the end of a working day placing them to the separate directory ("/MetaTraderServer/confirms/YYYYMMDD", where YYYYMMDD is current date). Each report is an HTML file having the name "login_mail.htm" (for example, "123_mail.htm"). After generating all reports, the trade server saves the configuration file ("mail.cfg") containing descriptions of account groups with e-mail settings in the same directory and then launches MetaTrader 5 SendMail utility.

## Operation Principles

After launching MetaTrader 5, SendMail reads the configuration file and starts sending emails to account groups. Description of each group contains data that is sufficient for authorization on the specified SMTP server. In case of an authorization error, the program simply moves to the next group sending the appropriate error message to the journal. If authorization is successful, reports are consistently sent to these group's accounts.

Two types of errors may occur when sending reports. First, connection to the SMTP server may be lost. In this case, an attempt to handle the next group is made. Second, the server may report that it is not able to send a report to the specified client address (for example, if the latter is incorrect). In this case, the report is marked as unsent and handling is moved to the next one.

After all MetaTrader 5 groups are handled, SendMail records the results in the same configuration file. Then all the reports and the configuration file are compressed into a ZIP file. ZIP file's name is based on the name of a low-level folder in the path to the reports (for example, if the path is "C:\mt5\trade_server\confirms\20130101", then ZIP file's name is "20130101.zip"). After the successful archiving, all source files are deleted.

> Attention: We strongly recommend to use your own mail server (at least having the  name)

# Sending Reports Manually

Reports may be sent manually in two modes: group and individual ones. To choose the mode, one of the keys should additionally be specified in the command line when launching MetaTrader 5 SendMail:

  * mt5sendmail64.exe /mail:[path] — individual mailing.
  * mt5sendmail64.exe /group:[path] — group mailing.
  * /archive — specify this key after /mail:[path] or /group:[path] to force the SendMail archive the reports after sending.



### Individual Mailing

MetaTrader 5 SendMail with "mail" key should be launched to send a report to a single user:

mt5sendmail64.exe /mail:"path" /archive  
---  
  
Path is the path to the directory containing folder.cfg mailing configuration file (the file should have exactly the name mentioned above). Do not add a backslash at the end of the path:

mt5sendmail64.exe /mail: "C:\MetaTrader 5 Platform\MainTrade\confirms\2021.05.11.daily" /archive  
---  
  
Here is an example of a configuration file structure:

from=abc@company.net  
name=ABC Company  
subject=Trade Report  
to=johnsmith@mail.net  
to_name=John Smith  
charset=utf-8  
body=D:\Reports\John_Smith\mail.htm  
attachments=D:\Reports\John_Smith\balance.jpg  
smtp_srv=abc@company.net  
smtp_login=mailer  
smtp_pass=mailerpassword  
---  
  
The following parameters are specified in the configuration file:

  * from — e-mail address, from which the report is sent.
  * name — sender's name.
  * subject — email subject.
  * to — recipient's email address.
  * to_name — recipient's name.
  * charset — email's character set.
  * body — path to the HTM file containing the email's contents.
  * attachments — path to the file that is to be attached to the email. If you want to attach several files, specify paths to them divided by tab. The line length, including the parameter name, should not exceed 256 characters.
  * smtp_srv — SMTP server address used for sending messages.
  * smtp_login — login for authorization on the mail server. In most cases, it is a mailbox, for example, "your_name@mail.ru".
  * smtp_pass — password for authorization on the mail server (mailbox password).



  * Up to 8 attachments can be added to an email.
  * Attachment size may not exceed 4 MB.
  * The password for authorization on the SMTP server is stored in the clear. This is done in order to modify the configuration file easily. The administrator can change the configuration (for example, a password) and launch SendMail manually. For security purposes, it is recommended to limit access to report configuration files.

  
---  
  
### Group Mailing

MetaTrader 5 SendMail with "group" key should be launched to send a report to a group of users:

mt5sendmail64.exe /group:"path" /archive  
---  
  
Path is a path to mail.cfg file (the file should have exactly the name mentioned above) containing description of mailing settings.

> Report files being sent should be in the same directory with  configuration file. The report for each user should be in the form of an HTM file named  (for example, ).

Here is an example of a configuration file structure:

<group>  
name=demoforex  
company=MetaQuotes Software Corp.  
email=reporter@metaquotes.ru  
subject=Trade Report  
smtp_srv=mail.metaquotes.ru  
smtp_login=reporter  
smtp_pass=securepass  
  
101 1 John Smith jjohnsmith@mail.ru  
102 1 Ivan Ivanov ivan@mail.ru  
103 2 Larisa Ivanovna larisa@mail.ru  
</group>  
  
<group>  
name=forever  
company=MetaQuotes Software Corp.  
email=mailer@metaquotes.ru  
smtp_srv=mail.metaquotes.ru  
smtp_login=mailer  
smtp_pass=mailerpassword  
  
151 0 Alisa alisa@pole.ru  
152 0 Brom brom@fix.com  
153 0 SirX sirx@fix.com  
</group>  
---  
  
Each target user group is described by a couple of <group> tags. Description of each group contains several mandatory fields:

  * name — group name.
  * company — company name that will be specified as a sender's name.
  * email — e-mail address, on behalf of which the report is sent.
  * subject — email subject.
  * smtp_srv — SMTP server address used for sending messages.
  * smtp_login — login for authorization on the mail server. In most cases, it is a mailbox, for example, "your_name@mail.ru".
  * smtp_pass — password for authorization on the mail server (mailbox password).



> The password for authorization on the SMTP server is stored in the clear. This is done in order to modify the configuration file easily. The administrator can change the configuration (for example, a password) and launch SendMail manually. For security purposes, it is recommended to limit access to report configuration files.

The group's description is followed by the list of users that should receive the reports. The description and the list should be divided by an empty line used as a separator.

Each entry in the user list consists of the four fields: login, mailing status, recipient name and email. Tab character is used as a field separator. The first field may contain spaces before its contents. Let's examine a sample entry in more details:

102 1 Ivan Ivanov ivan@mail.ru  
---  
  
Status ID may have the following values:

  * 0 — report has not been sent or is on hold.
  * 1 — report has been sent successfully.
  * 2 — report delivery error, invalid recipient e-mail address.



After the reports have been sent, mailing status is updated in the same configuration file.
