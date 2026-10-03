[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon Enumerations

[Previous](../IMTCon.md) | [Next](IMTCon-Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConFirewall](../IMTCon.md) class contains one enumeration.

<a id="enaction"></a>
## IMTConFirewall::EnAction (#enaction)

Types of actions that can be performed in accordance with a firewall rule are listed in IMTConFirewall::EnAction.

ID | Value | Description  
ACCESS_BLOCK | 0 | The blocking instruction.  
ACCESS_PERMIT | 1 | A permitting instruction.  
ACCESS_WHITELIST | 2 | The "Permit always" instruction. Such an instruction indicates the range of addresses that are allowed to access always, regardless of the blocking instruction and antfilud control.  
ACCESS_FIRST |  | Beginning of enumeration. It corresponds to ACCESS_BLOCK.  
ACCESS_LAST |  | End of enumeration. It corresponds to ACCESS_WHITELIST.  
  
This enumeration is used in the [IMTConFirewall::Action](IMTCon-Action.md) method.
