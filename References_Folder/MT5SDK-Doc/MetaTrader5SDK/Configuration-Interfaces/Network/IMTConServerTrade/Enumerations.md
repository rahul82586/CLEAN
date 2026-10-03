[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / Enumerations

[Previous](../IMTConServerTrade.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConServerTrade](../IMTConServerTrade.md) contains the following enumerations:

  * [IMTConServerTrade::EnDemoMode (#endemomode)](Enumerations.md#endemomode)
  * [IMTConServerTrade::EnOvernightMode (#enovernightmode)](Enumerations.md#enovernightmode)
  * [IMTConServerTrade::EnOvermonthMode (#enovermonthmode)](Enumerations.md#enovermonthmode)
  * [IMTConServerTrade::EnOvernightDays (#enovernightdays)](Enumerations.md#enovernightdays)



<a id="endemomode"></a>
## IMTConServerTrade::EnDemoMode (#endemomode)

Demo account allocation modes are specified in IMTConServerTrade::EnDemoMode.

ID | Value | Description  
DEMO_DISABLED | 0 | Creation of demo accounts is disabled.  
DEMO_PROLONG | 1 | Prolong the period of demo accounts after connection.  
DEMO_FIXED | 2 | Demo accounts with a fixed expiration date.  
DEMO_FIRST |  | Beginning of enumeration. It corresponds to DEMO_DISABLED.  
DEMO_LAST |  | End of enumeration. Corresponds to DEMO_LAST.  
  
This enumeration is used in the [IMTConServerTrade::DemoMode](DemoMode.md) method.

<a id="enovernightmode"></a>
## IMTConServerTrade::EnOvernightMode (#enovernightmode)

Modes of transition to the next day are enumerated in IMTConServerTrade::EnOvernightMode.

ID | Value | Description  
OVERNIGHT_END_DAY | 0 | At the end of the day.  
OVERNIGHT_START_DAY | 1 | At the beginning of the day.  
OVERNIGHT_FIRST |  | Beginning of enumeration. It corresponds to OVERNIGHT_END_DAY.  
OVERNIGHT_LAST |  | End of enumeration. It corresponds to OVERNIGHT_START_DAY.  
  
This enumeration is used in the [IMTConServerTrade::OvernightMode](OvernightMode.md) method.

<a id="enovermonthmode"></a>
## IMTConServerTrade::EnOvermonthMode (#enovermonthmode)

Modes of transition to the next month are enumerated in IMTConServerTrade::EnOvermonthMode.

ID | Value | Description  
OVERMONTH_LAST_DAY | 0 | On the last day of the month.  
OVERMONTH_FIRST_DAY | 1 | On the first day of the month.  
OVERMONTH_FIRST |  | Beginning of enumeration. It corresponds to OVERMONTH_LAST_DAY.  
OVERMONTH_LAST |  | End of enumeration. It corresponds to OVERMONTH_FIRST_DAY.  
  
This enumeration is used in the [IMTConServerTrade::OvermonthMode](OvermonthMode.md) method.

<a id="enovernightdays"></a>
## IMTConServerTrade::EnOvernightDays (#enovernightdays)

IMTConServerTrade::EnOvernightDays contains the flags of the days, on which operations related to the end of a trading day are performed. Report generation, swap calculation, annual interest and commission operations are only performed on these days. These flags do not affect monthly reports.

ID | Value | Description  
| Enumeration of days, in which end-of-day operations are performed.  
OVERNIGHT_DAYS_SUN | 0x00000001 | Sunday.  
OVERNIGHT_DAYS_MON | 0x00000002 | Monday.  
OVERNIGHT_DAYS_TUE | 0x00000004 | Tuesday.  
OVERNIGHT_DAYS_WED | 0x00000008 | Wednesday.  
OVERNIGHT_DAYS_THU | 0x00000010 | Thursday.  
OVERNIGHT_DAYS_FRI | 0x00000020 | Friday.  
OVERNIGHT_DAYS_SAT | 0x00000040 | Saturday.  
| Enumeration of days, in which rollover charging is performed.  
OVERNIGHT_DAYS_ROLLOVER_SUN | 0x00000080 | Sunday.  
OVERNIGHT_DAYS_ROLLOVER_MON | 0x00000100 | Monday.  
OVERNIGHT_DAYS_ROLLOVER_TUE | 0x00000200 | Tuesday.  
OVERNIGHT_DAYS_ROLLOVER_WED | 0x00000400 | Wednesday.  
OVERNIGHT_DAYS_ROLLOVER_THU | 0x00000800 | Thursday.  
OVERNIGHT_DAYS_ROLLOVER_FRI | 0x00001000 | Friday.  
OVERNIGHT_DAYS_ROLLOVER_SAT | 0x00002000 | Saturday.  
OVERNIGHT_DAYS_NONE | 0x00000000 | Beginning of enumeration. It corresponds to the absence of flags.  
OVERNIGHT_DAYS_DEFAULT |  | Default flags. Corresponds to days from Monday to Friday.  
OVERNIGHT_DAYS_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConServerTrade::OvernightDays](OvernightDays.md) method.
