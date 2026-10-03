[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / EmailSend

[Previous](NotificationsSend.md) | [Next](MessengerVerifyPhone.md)

# IMTManagerAPI::EmailSend

Send an email to a selected address.

C++
    
    
    MTAPIRES  IMTManagerAPI::EmailSend(
       LPCWSTR      account,      // Mail account used to send the email
       LPCWSTR      to,           // Recipient address
       LPCWSTR      to_name,      // Recipient name
       LPCWSTR      subject,      // Email subject
       LPCWSTR      body          // Email body
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.EmailSend(
       string       account,      // Mail account used to send the email
       string       to,           // Recipient address
       string       to_name,      // Recipient name
       string       subject,      // Email subject
       string       body          // Email body
       )

Python
    
    
    ManagerAPI.EmailSend(
       account,     # Mail account used to send the email
       to,          # Recipient address
       to_name,     # Recipient name
       subject,     # Email subject
       body         # Email body
       )

### Program Parameters

**account**  
[in] The name of the mail server configuration, via which the email will be sent. TheIMTConEmail::Namevalue is used for the name.

**to**  
[in] Recipient's email address.

**to_name**  
[in] Email recipient's name.

**subject**  
[in] Email subject.

**body**  
[in] Email body.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

All method parameters are required.
