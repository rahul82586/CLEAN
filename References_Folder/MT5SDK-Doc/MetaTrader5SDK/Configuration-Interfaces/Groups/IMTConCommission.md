[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Groups](../Groups.md) / IMTConCommission

[Previous](IMTConGroupSink/HookGroupDelete.md) | [Next](IMTConCommission/Enumerations.md)

# IMTConCommission

The IMTConCommission class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConCommission/Release.md) | Delete the current object.  
[Assign](IMTConCommission/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConCommission/Clear.md) | Clear an object.  
[Name](IMTConCommission/Name.md) | Get and set the commission configuration name.  
[Description](IMTConCommission/Description.md) | Get and set the description of the commission configuration.  
[Path](IMTConCommission/Path.md) | Get and set the path to a symbol or group of symbols that are subject to commission.  
[Mode](IMTConCommission/Mode.md) | Get and set the commission type.  
[RangeMode](IMTConCommission/RangeMode.md) | Get and set the type of commission ranges - by trade volume or turnover.  
[ChargeMode](IMTConCommission/ChargeMode.md) | Get and set the commission charging time.  
[EntryMode](IMTConCommission/EntryMode.md) | Get and set commission calculation mode depending on the deal direction.  
[ActionMode](IMTConCommission/ActionMode.md) | Get and set commission calculation mode depending on the deal type.  
[ProfitMode](IMTConCommission/ProfitMode.md) | Get and set commission calculation mode depending on the deal profit.  
[ReasonFlags](IMTConCommission/ReasonFlags.md) | Get and set commission calculation mode depending on the reason for the deal execution.  
[TurnoverCurrency](IMTConCommission/TurnoverCurrency.md) | Get and set the currency, in which the money turnover is calculated.  
[TierAdd](IMTConCommission/TierAdd.md) | Add commission range.  
[TierUpdate](IMTConCommission/TierUpdate.md) | Update commission range.  
[TierDelete](IMTConCommission/TierDelete.md) | Delete a commission range by the index.  
[TierClear](IMTConCommission/TierClear.md) | Clear the list of commission ranges.  
[TierShift](IMTConCommission/TierShift.md) | Moves a commission range in the list.  
[TierTotal](IMTConCommission/TierTotal.md) | Get the number of commission ranges.  
[TierNext](IMTConCommission/TierNext.md) | Get a commission range by the index.  
  
The IMTConCommission class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnCommMode (#encommmode)](IMTConCommission/Enumerations.md#encommmode) | Type of commission — standard or agent.  
[EnCommRangeMode (#encommrangemode)](IMTConCommission/Enumerations.md#encommrangemode) | Type of commission ranges — by trade volume or turnover.  
[EnCommChargeMode (#encommchargemode)](IMTConCommission/Enumerations.md#encommchargemode) | Charging mode — instant, at the end of the day or at the end of the month.  
[EnCommEntryMode (#encommentrymode)](IMTConCommission/Enumerations.md#encommentrymode) | Commission mode depending on the direction of deals.  
[EnCommActionMode (#encommactionmode)](IMTConCommission/Enumerations.md#encommactionmode) | Commission mode depending on the deal type.  
[EnCommProfitMode (#encommprofitmode)](IMTConCommission/Enumerations.md#encommprofitmode) | Commission charging mode depending on the deal profit.  
[EnCommReasonFlags (#encommreasonflags)](IMTConCommission/Enumerations.md#encommreasonflags) | Commission charging mode depending on the deal execution reasons.
