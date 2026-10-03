[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerSend

[Previous](MessengerVerifyPhone.md) | [Next](../Automation.md)

# IMTAdminAPI::MessengerSend

Send an SMS message.

C++
    
    
    MTAPIRES  IMTAdminAPI::MessengerSend(
       LPCWSTR      destination,  // Phone number
       LPCWSTR      group,        // Group
       LPCWSTR      sender,       // Sender
       LPCWSTR      text          // Message text
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MessengerSend(
       string       destination,  // Phone number
       string       group,        // Group
       string       sender,       // Sender
       string       text          // Message text
       )

Python
    
    
    AdminAPI.MessengerSend(
       destination, # Phone number
       group,       # Group
       sender,      # Sender
       text         # Message text
       )

### Program Parameters

**destination**  
[in] Recipient's phone number in the format +[country code][number], for example: +74951113594. The number is indicated without spaces.

**group**  
[in] Here you can specify the group to which the message recipient's account belongs. In this case, the platform will send the message through the first provider, in whosesettingsthe specified group is found. The parameter is optional: is NULL is specified, the provider will be selected without regard to the group.

**sender**  
[in] The name of the message sender. It is only used if the appropriate function is supported by the provider. This parameter is optional (NULL can be passed).

**text**  
[in] The text of the notification. The maximum allowable length depends on the provider.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) does not indicate the successful message delivery.
