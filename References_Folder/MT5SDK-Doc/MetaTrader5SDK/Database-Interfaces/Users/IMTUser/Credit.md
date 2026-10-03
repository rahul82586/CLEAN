[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Credit

[Previous](EquityPrevMonth.md) | [Next](LimitOrders.md)

# IMTUser::Credit

Get the current amount of funds credited to a client.

C++
    
    
    double  IMTUser::Credit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTUser.Credit()

### Return Value

The current amount of funds credited to the client.

### Note

Client's credit funds are the total sum of all operations of the "Credit" ([EnDealAction::DEAL_CREDIT (#endealaction)](../../Trade/Deals/IMTDeal/Enumerations.md#endealaction)) and "Bonus" ([EnDealAction::DEAL_BONUS (#endealaction)](../../Trade/Deals/IMTDeal/Enumerations.md#endealaction)).
