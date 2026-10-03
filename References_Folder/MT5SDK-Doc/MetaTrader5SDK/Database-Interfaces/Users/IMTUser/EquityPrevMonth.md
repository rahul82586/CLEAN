[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / EquityPrevMonth

[Previous](EquityPrevDay.md) | [Next](Credit.md)

# IMTUser::EquityPrevMonth

Get the value of a client's equity as of the end of the previous trading month.

C++
    
    
    double  IMTUser::EquityPrevMonth()

.NET (Gateway/Manager API)
    
    
    double  CIMTUser.EquityPrevMonth()

### Return Value

The value of a client's equity as of the end of the previous trading month.

### Note

The trade server updates the field value when switching to the next trading month ([IMTConServerTrade::OvermonthMode](../../../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md)). No update is performed for demo accounts from groups for which the generation of daily reports is disabled ([IMTConGroup::REPORTS_DISABLED (#enreportsmode)](../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enreportsmode)).
