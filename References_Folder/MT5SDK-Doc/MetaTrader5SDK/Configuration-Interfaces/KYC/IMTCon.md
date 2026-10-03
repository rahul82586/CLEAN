[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [KYC](../KYC.md) / IMTCon

[Previous](../KYC.md) | [Next](IMTConKYC/IMTCon-Enumerations.md)

# IMTConKYC

The IMTConKYC class contains methods for getting and editing KYC provider configurations:

Method | Purpose  
---|---  
[Release](IMTConKYC/IMTCon-Release.md) | Delete the current object.  
[Assign](IMTConKYC/IMTCon-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConKYC/IMTCon-Clear.md) | Clear an object.  
[Name](IMTConKYC/IMTCon-Name.md) | Get and set the name of the KYC provider configuration.  
[ProviderType](IMTConKYC/IMTCon-ProviderType.md) | Get and set the KYC service provider in the configuration.  
[ProviderAddress](IMTConKYC/IMTCon-ProviderAddress.md) | Get and set the KYC provider's server address in the configuration.  
[ProviderLogin](IMTConKYC/IMTCon-ProviderLogin.md) | Get and set the login of the account used for connecting to the KYC-provider.  
[ProviderPassword](IMTConKYC/IMTCon-ProviderPassword.md) | Get and set the password of the account used for connecting to the KYC-provider.  
[ProviderToken](IMTConKYC/IMTCon-ProviderToken.md) | Get and set the authorization token used for connection to the KYC provider.  
[Flags](IMTConKYC/IMTCon-Flags.md) | Get and set additional settings of the KYC provider.  
[CountryAdd](IMTConKYC/IMTCon-CountryAdd.md) | Add a country for which the KYC provider will be used.  
[CountryUpdate](IMTConKYC/IMTCon-CountryUpdate.md) | Change the country for which the KYC provider is used.  
[CountryDelete](IMTConKYC/IMTCon-CountryDelete.md) | Delete the country for which the KYC provider is used.  
[CountryClear](IMTConKYC/IMTCon-CountryClear.md) | Clear the list of countries for which the KYC provider is used.  
[CountryShift](IMTConKYC/IMTCon-CountryShift.md) | Shift a country in the KYC provider settings.  
[CountryTotal](IMTConKYC/IMTCon-CountryTotal.md) | Get the number of countries specified in the KYC provider settings.  
[CountryNext](IMTConKYC/IMTCon-CountryNext.md) | Get the country for which the KYC provider is used by its index in the list.  
[GroupAdd](IMTConKYC/IMTCon-GroupAdd.md) | Add a group of accounts for which the KYC provider will be used.  
[GroupUpdate](IMTConKYC/IMTCon-GroupUpdate.md) | Change the group of accounts for which the KYC provider is used.  
[GroupDelete](IMTConKYC/IMTCon-GroupDelete.md) | Delete the group of accounts for which the KYC provider is used.  
[GroupClear](IMTConKYC/IMTCon-GroupClear.md) | Clear the list of groups for which the KYC provider is used.  
[GroupShift](IMTConKYC/IMTCon-GroupShift.md) | Shift a group in the KYC provider settings.  
[GroupTotal](IMTConKYC/IMTCon-GroupTotal.md) | Get the number of groups specified in the KYC provider settings.  
[GroupNext](IMTConKYC/IMTCon-GroupNext.md) | Get the group for which the KYC provider is used by its index in the list.  
  
The IMTConKYC class contains the following enumerations:

Enumeration | Description  
---|---  
[EnFlags (#enflags)](IMTConKYC/IMTCon-Enumerations.md#enflags) | KYC provider configuration flags.  
[EnProviderType (#enprovidertype)](IMTConKYC/IMTCon-Enumerations.md#enprovidertype) | Supported providers.
