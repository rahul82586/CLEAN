[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Messengers](../Messengers.md) / IMTConMessenger

[Previous](../Messengers.md) | [Next](IMTConMessenger/Enumerations.md)

# IMTConMessenger

The IMTConMessenger class contains methods for getting and updating messenger configurations:

Method | Purpose  
---|---  
[Release](IMTConMessenger/Release.md) | Delete the current object.  
[Assign](IMTConMessenger/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConMessenger/Clear.md) | Clear an object.  
[Name](IMTConMessenger/Name.md) | Get and set the messenger configuration name.  
[Sender](IMTConMessenger/Sender.md) | Get and set the sender name in the messenger configuration.  
[ProviderType](IMTConMessenger/ProviderType.md) | Get and set the messaging service provider in the messenger configuration.  
[ProviderAddress](IMTConMessenger/ProviderAddress.md) | Get and set the messaging provider server address in the messenger configuration.  
[ProviderLogin](IMTConMessenger/ProviderLogin.md) | Get and set the login of the account which is used for sending messages via the messenger.  
[ProviderPassword](IMTConMessenger/ProviderPassword.md) | Get and set the password of the account which is used for sending messages via the messenger.  
[ProviderToken](IMTConMessenger/ProviderToken.md) | Get and set the authentication token, which is used for sending messages via the messenger.  
[ProviderSubId](IMTConMessenger/ProviderSubId.md) | Get and set the sender identifier, which is used for sending messages via the messenger.  
[ProviderCurrency](IMTConMessenger/ProviderCurrency.md) | Get and set the currency which is used for service provider pricing.  
[ProviderCurrencyRate](IMTConMessenger/ProviderCurrencyRate.md) | Get and set the rate at which the currency of service provider pricing is converted to US dollars.  
[Flags](IMTConMessenger/Flags.md) | Get and set additional messenger settings.  
[MessageTemplate](IMTConMessenger/MessageTemplate.md) | Get and set a basic template for sending messages via this provider.  
[CountryAdd](IMTConMessenger/CountryAdd.md) | Add a country for which the messenger will be used.  
[CountryUpdate](IMTConMessenger/CountryUpdate.md) | Change the country for which the messenger is used.  
[CountryDelete](IMTConMessenger/CountryDelete.md) | Delete the country for which the messenger is used.  
[CountryClear](IMTConMessenger/CountryClear.md) | Clear the list of countries for which the messenger is used.  
[CountryShift](IMTConMessenger/CountryShift.md) | Shift a country in the messenger settings.  
[CountryTotal](IMTConMessenger/CountryTotal.md) | Get the number of countries specified in the messenger settings.  
[CountryNext](IMTConMessenger/CountryNext.md) | Get the country for which the messenger is used, by its index in the list.  
[GroupAdd](IMTConMessenger/GroupAdd.md) | Add a group of accounts for which the messenger will be used.  
[GroupUpdate](IMTConMessenger/GroupUpdate.md) | Change the group of accounts for which the messenger is used.  
[GroupDelete](IMTConMessenger/GroupDelete.md) | Delete the group of accounts for which the messenger is used.  
[GroupClear](IMTConMessenger/GroupClear.md) | Clear the list of groups for which the messenger is used.  
[GroupShift](IMTConMessenger/GroupShift.md) | Shift a group in the messenger settings.  
[GroupTotal](IMTConMessenger/GroupTotal.md) | Get the number of groups specified in the messenger settings.  
[GroupNext](IMTConMessenger/GroupNext.md) | Get the group for which the messenger is used, by its index in the list.  
[TemplateAdd](IMTConMessenger/TemplateAdd.md) | Add a message template that the messenger will use.  
[TemplateUpdate](IMTConMessenger/TemplateUpdate.md) | Edit the message template used by the messenger.  
[TemplateDelete](IMTConMessenger/TemplateDelete.md) | Delete the message template used by the messenger.  
[TemplateClear](IMTConMessenger/TemplateClear.md) | Clear the list of message templates used by the messenger.  
[TemplateShift](IMTConMessenger/TemplateShift.md) | Move the message template in the messenger settings.  
[TemplateTotal](IMTConMessenger/TemplateTotal.md) | Get the number of message templates specified in the messenger settings.  
[TemplateNext](IMTConMessenger/TemplateNext.md) | Get a message template used by the messenger by its index in the list.  
  
The IMTConMessenger class contains the following enumerations:

Enumeration | Description  
---|---  
[EnFlags (#enflags)](IMTConMessenger/Enumerations.md#enflags) | Messenger configuration flags.  
[EnProviderType (#enprovidertype)](IMTConMessenger/Enumerations.md#enprovidertype) | Supported providers.
