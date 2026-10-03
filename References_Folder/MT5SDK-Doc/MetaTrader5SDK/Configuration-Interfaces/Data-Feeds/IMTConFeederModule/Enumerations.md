[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Enumerations

[Previous](../IMTConFeederModule.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConFeederModule](../IMTConFeederModule.md) calss contains one enumeration:

<a id="enfeedersfieldflags"></a>
## IMTConFeederModule::EnFeedersFieldFlags (#enfeedersfieldflags)

Flags of editable fields are listed in IMTConFeederModule::EnFeedersFieldFlags.

ID | Value | Description  
FEED_FIELD_SERVER | 1 | The "Server" field.  
FEED_FIELD_LOGIN | 2 | The "Login" field.  
FEED_FIELD_PASS | 4  | The "Password" field.  
FEED_FIELD_PARAM | 8 | The "Parameters" field.  
FEED_FIELD_NONE | 0 | Beginning of enumeration. It corresponds to the absence of required fields.  
FEED_FIELD_ALL |  | End of enumeration. It corresponds to the fact that all fields are required.  
  
This enumeration is used in the [IMTConFeederModule::Modes](Modes.md) method.
