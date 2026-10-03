[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Enumerations

[Previous](../IMTConEmail.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConEmail](../IMTConEmail.md) class contains one enumeration:

<a id="enflags"></a>
## IMTConEmail::EnFlags (#enflags)

The IMTConEmail::EnFlags enumeration contains mail server configuration flags.

Identifier | Value | Description  
FLAG_NONE | 0 | No flags.  
FLAG_ENABLED | 1 | The mail server configuration is enabled. If the flag is not set, emails will not be sent via this server.  
FLAG_DEFAULT | 2 | Default mail server. The special "Default" option can be selected for the used mail server in group settings ([IMTConGroup::ReportsEmail](../../Groups/IMTConGroup/ReportsEmail.md)) and account allocation settings. In this case the platform will check the list of all servers and will send emails via the first available server with the FLAG_DEFAULT enabled.  
FLAG_FIRST |  | Beginning of enumeration. Corresponds to FLAG_NONE.  
FLAG_ALL |  | End of enumeration. All flags are enabled.  
  
The enumeration is used in the [IMTConEmail::Flags](Flags.md) methods.
