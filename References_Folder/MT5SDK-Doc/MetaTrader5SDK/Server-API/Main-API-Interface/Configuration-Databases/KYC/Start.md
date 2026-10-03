[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Start

[Previous](Get.md) | [Next](../Subscriptions.md)

# IMTServerAPI::KYCStart

Run a KYC check for the specified client.
    
    
    MTAPIRES  IMTServerAPI::KYCStart(
       const UINT64      client_id  // Client id
       )

### Parameters

**client_id**  
[in] The identifier of the client for whom the check should be run. The client ID is equal to theIMTClient::RecordIDvalue.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The KYC provider through which the check will be performed, is selected based on the client's country and group. For further information, please see [MetaTrader 5 Administrator Help (#best-provider)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/integration/integration_kyc#best-provider).
