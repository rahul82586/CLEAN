[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Enumerations

[Previous](../Requests-IMTConfirm.md) | [Next](Requests-Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConfirm](../Requests-IMTConfirm.md) class contains one enumeration:

<a id="enconfirmflags"></a>
## IMTConfirm::EnConfirmFlags (#enconfirmflags)

Possible options of request confirmation are listed in IMTConfirm::EnConfirmFlags.

ID | Value | Description  
CONFIRM_FLAG_NONE | 0 | No confirmation options.  
CONFIRM_FLAG_TICK | 1 | Adding the price at which the request is executed to the stream of quotes.  
CONFIRM_FLAG_ALL |  | Enabling all options.  
  
This enumeration is used in the [IMTConfirm::Flags](Requests-Flags.md) method.
