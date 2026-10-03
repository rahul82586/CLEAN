[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / Data Structure

[Previous](../Messengers.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A messenger configuration is passed in JSON format in response to the [/api/messenger/add](Add.md), [/api/messenger/next](Get-by-Index.md) and [/api/messenger/get](Get-by-Name.md) requests.

Parameter | Type | Purpose  
Name | String | Messenger configuration name.  
Sender | String | The sender name in the messenger configuration.  
ProviderType | Integer | The messaging service provider in the messenger configuration. Passed as a value of the [EnProviderType (#enprovidertype)](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Enumerations.md#enprovidertype) enumeration.  
ProviderAddress | String | The provider's server address in a messenger configuration.  
ProviderLogin | String | The login of the account which is used for sending messages via the messenger.  
ProviderPassword | String | The password of the account which is used for sending messages via the messenger.  
ProviderToken | String | The authentication token, which is used for sending messages via the messenger.  
ProviderSubId | String | The sender identifier, which is used for sending messages via the messenger.  
ProviderCurrency | String | The currency for service provider's pricing.  
ProviderCurrencyRate | Float | The rate at which the service pricing currency is converted to US dollars.  
Flags | Integer | Additional messenger settings. Passed using the [EnFlags (#enflags)](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Enumerations.md#enflags) enumeration.  
Countries | Array | [The list of countries (#country)](Data-Structure.md#country), for which this messenger is used.  
Groups | Array | [The list of groups (#group)](Data-Structure.md#group), for which this messenger is used.  
  
<a id="country"></a>
## Countries (#country)

Parameter | Type | Purpose  
PhoneCode | Integer | Country phone code.  
  
<a id="group"></a>
## Groups (#group)

Parameter | Type | Purpose  
Group | String | Full path to the group.  
Sender | String | Message sender name.
