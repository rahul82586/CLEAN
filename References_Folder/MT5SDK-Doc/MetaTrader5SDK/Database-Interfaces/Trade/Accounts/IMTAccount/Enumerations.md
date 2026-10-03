[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Enumerations

[Previous](../IMTAccount.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTAccount](../IMTAccount.md) class contains one enumeration:

<a id="ensoactivation"></a>
## IMTAccount::EnSoActivation (#ensoactivation)

The account status as per the minimum amount of funds on the account required to maintain trading positions are enumerated in IMTAccount::EnSoActivation.

ID | Value | Description  
ACTIVATION_NONE | 0 | None.  
ACTIVATION_MARGIN_CALL | 1 | Margin call.  
ACTIVATION_STOP_OUT | 2 | Stop out.  
ACTIVATION_FIRST |  | Beginning of enumeration. It corresponds to ACTIVATION_NONE.  
ACTIVATION_LAST |  | End of enumeration. It corresponds to ACTIVATION_STOP_OUT.  
  
This enumeration is used in the [IMTAccount::SOActivation](SOActivation.md) method.
