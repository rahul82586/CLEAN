[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / BalancePrevDay

[Previous](Balance.md) | [Next](BalancePrevMonth.md)

# IMTUser::BalancePrevDay

Get the value of a client's balance as of the end of the previous day.

C++
    
    
    double  IMTUser::BalancePrevDay()

.NET (Gateway/Manager API)
    
    
    double  CIMTUser.BalancePrevDay()

### Return Value

A client's balance as of the end of the previous day.

### Note

The trade server updates the field value when switching to the next trading day ([IMTConServerTrade::OvernightTime](../../../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md)). No update is performed for demo accounts from groups for which the generation of daily reports is disabled ([IMTConGroup::REPORTS_DISABLED (#enreportsmode)](../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enreportsmode)).
