[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / Data Structure

[Previous](../Subscriptions.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Subscription configuration is passed in JSON format as a response to the [/api/subscription/config/add](Add.md), [/api/subscription/config/next](Get-by-Index.md) and [/api/subscription/config/get](Get-by-NameID.md) requests.

<a id="subscription"></a>
## General Subscription Paramers (#subscription)

Parameter | Type | Description  
ID | Integer | Unique configuration identifier.  
ParentID | Integer | The identifier of the subdirectory in which the configuration is located.  
Type | Integer | Configuration type. The type is passed by the [EnType (#entype)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Enumerations.md#entype) enumeration.  
Name | String | Subscription name.  
URL | String | A link to an additional subscription description.  
AgreementURL | String | A link to a subscription agreement.  
Flags | Integer | Additional subscription settings. Additional settings are passed by the [EnFlags (#enflags)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Enumerations.md#enflags) enumeration.  
Control | Integer | Subscription management mode in client terminals (allowed actions). Modes are passed by the [EnControlMode (#encontrolmode)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Enumerations.md#encontrolmode) enumeration.  
Image | Integer | Subscription logo. Logos are passed by the [EnImageType (#enimagetype)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Enumerations.md#enimagetype) enumeration.  
ImageURL | String | A link to a custom subscription logo. The field is currently not used.  
Period  | Integer | Subscription period. The period is passed by the [EnPeriod (#enperiod)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Enumerations.md#enperiod) enumeration.  
PeriodCustom | Integer | Custom subscription period in days.  
FreePeriod | Integer | Trial (free) subscription period. The trial period if passed by the [EnFreePeriod (#enfreeperiod)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Enumerations.md#enfreeperiod) enumeration.  
FreePeriodCustom | Integer | Custom value for a trial (free) subscription period.  
Price | Float | Subscription price for non-professional traders.  
PriceCurrency | String | Currency in which the subscription price is specified.  
PriceProfessional | Float | Subscription price for professional traders.  
PriceCost | Float | Subscription cost.  
DependsID | Integer | ID of the subscription which the current subscription depends on.  
Description | String | Subscription description.  
Countries | Array | The list of two-letter codes of countries for which the subscription is available.  
Groups | Array | The list of groups for which the subscription is available.  
Symbols | Array | [Trading instruments (#symbols)](Data-Structure.md#symbols) available by subscription.  
News | Array | [News categories (#news)](Data-Structure.md#news) available by subscription.  
  
<a id="symbols"></a>
## Symbols (#symbols)

Parameter | Type | Description  
Level | Integer | The type of price data available by subscription. Price data type is passed by the [EnLevel (#enlevel)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSymbol/Enumerations.md#enlevel) enumeration.  
Symbols | Integer | Path to the symbol (group of symbols), the data for which is provided by subscription.  
TickHistory | Integer | Tick data depth available by subscription. Data depth is passed by the [EnTickHistory (#entickhistory)](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSymbol/Enumerations.md#entickhistory) enumeration.  
  
<a id="news"></a>
## News categories (#news)

Parameter | Type | Description  
Category | String | News categories available by subscription.  
Language | Integer | The language of news available by subscription.
