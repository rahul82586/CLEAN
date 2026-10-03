[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / EquityPrevDay

[Previous](BalancePrevMonth.md) | [Next](EquityPrevMonth.md)

# IMTUser::EquityPrevDay

Get the value of a client's equity as of the end of the previous day.

C++
    
    
    double  IMTUser::EquityPrevDay()

.NET (Gateway/Manager API)
    
    
    double  CIMTUser.EquityPrevDay()

### Return Value

A client's equity as of the end of the previous day.

### Note

The trade server updates the field value when switching to the next trading day ([IMTConServerTrade::OvernightTime](../../../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md)). No update is performed for demo accounts from groups for which the generation of daily reports is disabled ([IMTConGroup::REPORTS_DISABLED (#enreportsmode)](../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enreportsmode)).
