[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Email](../Email.md) / Data Structure

[Previous](../Email.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Mail server configuration is passed in JSON format in response to the [/api/email/add](Add.md), [/api/email/next](Get-by-Index.md) and [/api/email/get](Get-by-Name.md) requests.

Parameter | Type | Purpose  
Name | String | Mail server configuration name.  
SenderMail | String | The email address, from which emails are sent via the mail server configurations.  
SenderName | String | The sender name in the mail server configuration.  
Server | String | The SMTP server address in the mail server configuration.  
Login | String | The SMTP login in the mail server configuration.  
Password | String | The SMTP password in the mail server configuration.  
Flags | Integer | Advanced mail server settings. Passed using the [EnFlags (#enflags)](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmail/Enumerations.md#enflags) enumeration.  
Stats | Array | [Information (#statistics)](Data-Structure.md#statistics) about the mail server operation.  
  
<a id="statistics"></a>
## Statistics (#statistics)

Parameter | Type | Purpose  
TotalSend | Integer | The number of emails sent.  
TotalFailed | Integer | The number of unsent emails due to errors.  
CurrentQueue | Integer | The number of emails waiting to be sent.  
TimeMin | Integer | Minimum email sending time.  
TimeMax | Integer | Maximum email sending time.  
TimeAvg | Integer | Average email sending time.
