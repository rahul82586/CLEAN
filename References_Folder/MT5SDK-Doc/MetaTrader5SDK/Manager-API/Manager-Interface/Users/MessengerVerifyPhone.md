[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / MessengerVerifyPhone

[Previous](EmailSend.md) | [Next](MessengerSend.md)

# IMTManagerAPI::MessengerVerifyPhone

Verify the validity of a passed phone number based on local phone number formation rules.
    
    
    MTAPIRES  IMTManagerAPI::MessengerVerifyPhone (
       LPCWSTR     phone_number  // phone number
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.MessengerVerifyPhone(
       string      phone_number  // phone number
       )

Python
    
    
    ManagerAPI.MessengerVerifyPhone(
       phone_number  # phone number
       )

### Parameters

**phone_number**  
[in] Verified phone number. The phone number should be passed in the international format: +[country code] [phone number].

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
