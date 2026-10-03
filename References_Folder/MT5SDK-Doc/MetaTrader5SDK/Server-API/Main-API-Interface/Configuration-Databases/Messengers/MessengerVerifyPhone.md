[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerVerifyPhone

[Previous](MessengerGet.md) | [Next](MessengerSend.md)

# IMTServerAPI::MessengerVerifyPhone

Verify the validity of a passed phone number based on local phone number formation rules.
    
    
    MTAPIRES  IMTServerAPI::MessengerVerifyPhone (
       LPCWSTR     phone_number  // phone number
       )

### Parameters

**phone_number**  
[in] Verified phone number. The phone number should be passed in the international format: +[country code] [phone number].

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
