[🏠 Document Start](../README.md) / [Configuration Interfaces](README.md) / KYC

[Previous](VPS/IMTConVPSSink/IMTConSink-OnSync.md) | [Next](KYC/IMTCon.md)

# Integration with KYC providers

The trading platforms supports integrations with KYC providers for automated verification of clients' personal data and documents. This allows the automation of the account opening process:

  * The user requests an account from the terminal by filling our a simple form and uploading the relevant documents
  * The data is automatically verified through the KYC provider
  * A verification report is added to the client record, and the corresponding status is assigned to it
  * After a final check, the manager can move the account to the appropriate real group



For further information, please see [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_kyc).

The interfaces described in this section enable the management of KYC provider settings:

  * [IMTConKYC](KYC/IMTCon.md) — methods for getting and editing KYC provider configurations.
  * [IMTConKYCCountry](KYC/IMTConCountry.md) — methods for getting and editing country settings in KYC providers.
  * [IMTConKYCGroup](KYC/IMTConGroup.md) — methods for getting and editing groups settings in KYC providers.
  * [IMTConKYCSink](KYC/IMTConSink.md) — event handlers for changes in KYC provider configurations.


