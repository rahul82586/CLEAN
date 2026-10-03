[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Certificates](../Certificates.md) / UserCertConfirm

[Previous](UserCertDelete.md) | [Next](../Trade.md)

# IMTServerAPI::UserCertConfirm

Confirm the user certificate.
    
    
    MTAPIRES  IMTServerAPI::UserCertConfirm(
       const UINT64  login      // User's login
       )

### Parameters

**login**  
[in] The login of a user whose certificate needs to be confirmed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This function allows confirming certificates of accounts in the groups for which the appropriate mode is enabled. It is impossible to log in using a certificate until it is confirmed.
