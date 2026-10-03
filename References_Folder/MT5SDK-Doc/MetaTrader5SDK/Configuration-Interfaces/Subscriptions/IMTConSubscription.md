[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Subscriptions](../Subscriptions.md) / IMTConSubscription

[Previous](../Subscriptions.md) | [Next](IMTConSubscription/Enumerations.md)

# IMTConSubscription

The IMTConSubscription class contains method for getting and editing [subscription settings](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions):

Method | Purpose  
---|---  
[Release](IMTConSubscription/Release.md) | Delete the current object.  
[Assign](IMTConSubscription/Assign.md) | Assigns a passed object to the current one.  
[Clear](IMTConSubscription/Clear.md) | Clear an object.  
[ID](IMTConSubscription/ID.md) | Get a unique configuration identifier.  
[ParentID](IMTConSubscription/ParentID.md) | Get the ID of the subdirectory in which the configuration is located.  
[DependsID](IMTConSubscription/DependsID.md) | Get and set the subscription which the current subscription depends on.  
[Name](IMTConSubscription/Name.md) | Get and set a subscription name.  
[Type](IMTConSubscription/Type.md) | Get and set a subscription configuration type.  
[Image](IMTConSubscription/Image.md) | Get and set a subscription logo.  
[Description](IMTConSubscription/Description.md) | Get and set a subscription description.  
[URLDescription](IMTConSubscription/URLDescription.md) | Get and set a link to an additional subscription description.  
[URLAgreement](IMTConSubscription/URLAgreement.md) | Get and set a link to a subscription agreement.  
[ControlMode](IMTConSubscription/ControlMode.md) | Get and set a subscription management mode in client terminals (allowed actions).  
[PeriodMode](IMTConSubscription/PeriodMode.md) | Get and set a subscription period.  
[PeriodCustom](IMTConSubscription/PeriodCustom.md) | Get and set a custom subscription period.  
[PeriodFreeMode](IMTConSubscription/PeriodFreeMode.md) | Get and set a trial (free) subscription period.  
[PeriodFreeCustom](IMTConSubscription/PeriodFreeCustom.md) | Get and set a custom value for a trial (free) subscription period.  
[Flags](IMTConSubscription/Flags.md) | Get and set additional subscription settings.  
[Price](IMTConSubscription/Price.md) | Get and set a subscription price for non-professional traders.  
[PricePro](IMTConSubscription/PricePro.md) | Get and set a subscription price for professional traders.  
[PriceCost](IMTConSubscription/PriceCost.md) | Get and set a subscription cost.  
[PriceCurrency](IMTConSubscription/PriceCurrency.md) | Get and set the currency in which the subscription price is specified.  
[CountryAdd](IMTConSubscription/CountryAdd.md) | Add a country for which the subscription will be available.  
[CountryUpdate](IMTConSubscription/CountryUpdate.md) | Change a country for which the subscription is available.  
[CountryDelete](IMTConSubscription/CountryDelete.md) | Delete a country for which the subscription is available.  
[CountryClear](IMTConSubscription/CountryClear.md) | Clear the list of countries for which the subscription is available.  
[CountryShift](IMTConSubscription/CountryShift.md) | Shift a country for which the subscription is available.  
[CountryTotal](IMTConSubscription/CountryTotal.md) | Get the number of countries for which the subscription is available.  
[CountryNext](IMTConSubscription/CountryNext.md) | Get a country, for which the subscription is available, by index.  
[GroupAdd](IMTConSubscription/GroupAdd.md) | Add a group for which the subscription will be available.  
[GroupUpdate](IMTConSubscription/GroupUpdate.md) | Change a group for which the subscription is available.  
[GroupDelete](IMTConSubscription/GroupDelete.md) | Delete a group for which the subscription is available.  
[GroupClear](IMTConSubscription/GroupClear.md) | Clear the list of groups for which the subscription is available.  
[GroupShift](IMTConSubscription/GroupShift.md) | Shift a country for which the subscription is available.  
[GroupTotal](IMTConSubscription/GroupTotal.md) | Get the number of groups for which the subscription is available.  
[GroupNext](IMTConSubscription/GroupNext.md) | Get a group, for which the subscription is available, by index.  
[SymbolAdd](IMTConSubscription/SymbolAdd.md) | Add a trading instrument to the list of symbols available by subscription.  
[SymbolUpdate](IMTConSubscription/SymbolUpdate.md) | Update a trading instrument in the list of symbols available by subscription.  
[SymbolDelete](IMTConSubscription/SymbolDelete.md) | Delete a trading instrument from the list of symbols available by subscription.  
[SymbolClear](IMTConSubscription/SymbolClear.md) | Clear the list of trading instruments available by subscription.  
[SymbolShift](IMTConSubscription/SymbolShift.md) | Shift a trading instrument in the list in subscription settings.  
[SymbolTotal](IMTConSubscription/SymbolTotal.md) | Get the number of trading instruments available by subscription.  
[SymbolNext](IMTConSubscription/SymbolNext.md) | Get a trading instrument available by subscription, by index.  
[NewsAdd](IMTConSubscription/NewsAdd.md) | Add a news category to the news list available by subscription.  
[NewsUpdate](IMTConSubscription/NewsUpdate.md) | Edit a news category in the news list available by subscription.  
[NewsDelete](IMTConSubscription/NewsDelete.md) | Delete a news category from the news list available by subscription.  
[NewsClear](IMTConSubscription/NewsClear.md) | Clear the list of news categories available by subscription.  
[NewsShift](IMTConSubscription/NewsShift.md) | Shift a news category in the list in subscription settings.  
[NewsTotal](IMTConSubscription/NewsTotal.md) | Get the number of news categories available by subscription.  
[NewsNext](IMTConSubscription/NewsNext.md) | Get a news category available by subscription, by index.  
  
The IMTConSubscription class contains the following enumerations:

Enumeration | Description  
---|---  
[EnLevel (#entype)](IMTConSubscription/Enumerations.md#entype) | Types of subscription objects.  
[EnPeriod (#enperiod)](IMTConSubscription/Enumerations.md#enperiod) | Subscription periods.  
[EnFreePeriod (#enfreeperiod)](IMTConSubscription/Enumerations.md#enfreeperiod) | Subscription trial periods.  
[EnFlags (#enflags)](IMTConSubscription/Enumerations.md#enflags) | Flags for additional subscription properties.  
[EnControlMode (#encontrolmode)](IMTConSubscription/Enumerations.md#encontrolmode) | Subscription actions that can be performed in client terminals.  
[EnImageType (#enimagetype)](IMTConSubscription/Enumerations.md#enimagetype) | Logos that can be used for subscriptions.
