[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / KYC

[Previous](VPS/Set.md) | [Next](KYC/Create.md)

# Integration with KYC providers

The trading platforms supports integrations with KYC providers for automated verification of clients' personal data and documents. This allows the automation of the account opening process:

  * The user requests an account from the terminal by filling our a simple form and uploading the relevant documents
  * The data is automatically verified through the KYC provider
  * A verification report is added to the client record, and the corresponding status is assigned to it
  * After a final check, the manager can move the account to the appropriate real group



For further information, please see [MetaTrader 5 Administrator Help](https://support.metaquotes.net/ru/docs/mt5/platform/administration/integration/integration_kyc).

The functions described in this section enable the management of KYC provider configurations, as well as the subscription to and unsubscribing from events related to configuration changes.

Function | Purpose  
---|---  
[KYCCreate](KYC/Create.md) | Create a KYC provider configuration object.  
[KYCCountryCreate](KYC/CountryCreate.md) | Create an object of a country for which the KYC provider will be used.  
[KYCGroupCreate](KYC/GroupCreate.md) | Create an object of an account group for which the KYC provider will be used.  
[KYCSubscribe](KYC/Subscribe.md) | Subscribe to events and hooks associated with KYC provider configurations.  
[KYCUnsubscribe](KYC/Unsubscribe.md) | Unsubscribe from events and hooks associated with KYC provider configurations.  
[KYCUpdate](KYC/Update.md) | Add or update a KYC provider configuration.  
[KYCUpdateBatch](KYC/UpdateBatch.md) | Add or update a batch of KYC provider configurations.  
[KYCDelete](KYC/Delete.md) | Delete a KYC provider configuration by name or index.  
[KYCDeleteBatch](KYC/DeleteBatch.md) | Delete a batch of KYC provider configurations.  
[KYCShift](KYC/Shift.md) | Change the position of a KYC provider configuration in the list.  
[KYCTotal](KYC/Total.md) | Get the total number of KYC provider configurations existing in the platform.  
[KYCNext](KYC/Next.md) | Get a KYC provider configuration by index.  
[KYCGet](KYC/Get.md) | Get a KYC provider configuration by name.  
[KYCStart](KYC/Start.md) | Run a KYC check for the specified client.
