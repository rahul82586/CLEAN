[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Mail](../Mail.md) / Data Structure

[Previous](../Mail.md) | [Next](Send.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Emails are passed in the JSON format in response to the [/api/mail/get](Get-Without-Body.md) and [/api/mail/get_body](Get-With-Body.md) requests.

<a id="email"></a>
## Email (#email)

Field | Type | Description  
ID | Integer | Email identifier.  
Time | Integer | The time of email sending in seconds elapsed since 01.01.1970.  
From | Integer | The login of the email sender.  
FromName | String | The name of the email sender.  
To | Integer | The login of the email recipient.  
ToName | String | The name of the email recipient.  
AttachmentSize | Integer | The size of the email attachments in bytes.  
Subject | String | Get and set the subject of an email.  
Body | String | Email body in the Base64 format.  
  
<a id="attachment"></a>
## Attachment (#attachment)

Field | Type | Description  
Path | Integer | The path at which the attachment is located on the local disk.  
Content | Integer | Attachment contents in the Base64 format.
