[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / AgentMonthly

[Previous](AgentDaily.md) | [Next](BalancePrevDay.md)

# IMTDaily::AgentMonthly

Get from a daily report the size of agent [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged for a client's trade operations for the current month .

C++
    
    
    double  IMTDaily::AgentMonthly()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.AgentMonthly()

### Return Value

The total amount of agent commissions charged for a client's trade operations for the current month.

# IMTDaily::AgentMonthly

Set in a daily report the size of agent [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) for a client's trade operations for the current month.

C++
    
    
    MTAPIRES  IMTDaily::AgentMonthly(
       const double  agent      // Agent commissions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.AgentMonthly(
       double        agent      // Agent commissions
       )

### Parameters

**agent**  
[in] The total amount of agent commissions charged for a client's trade operations for the current month.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
