[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailSend

[Previous](EmailGet.md) | [Next](../Messengers.md)

# IMTServerAPI::EmailSend

Send an email to a selected address.
    
    
    MTAPIRES  IMTServerAPI::EmailSend(
       LPCWSTR      account,      // Mail account used to send the email
       LPCWSTR      to,           // Recipient address
       LPCWSTR      to_name,      // Recipient name
       LPCWSTR      subject,      // Email subject
       LPCWSTR      body          // Email body
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

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

All method parameters are required.
