[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon Enumerations

[Previous](../IMTCon.md) | [Next](IMTCon-Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConTime](../IMTCon.md) class contains one enumeration.

<a id="entimetablemode"></a>
## IMTConTime::EnTimeTableMode (#entimetablemode)

Platform operation modes are enumerated in IMTConTime::EnTimeTableMode.

ID | Value | Description  
TIME_MODE_DISABLED | 0 | Non-working day.  
TIME_MODE_ENABLED | 1 | Working day.  
TIME_MODE_FIRST |  | Beginning of enumeration. In corresponds to TIME_MODE_DISABLED.  
TIME_MODE_LAST |  | End of enumeration. It corresponds to TIME_MODE_ENABLED.  
  
This enumeration is used in the following methods:

  * [IMTConTime::TimeTableGet](IMTCon-TableGet.md)
  * [IMTConTime::TimeTableSet](IMTCon-TableSet.md)


