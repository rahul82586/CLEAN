[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / AgentDaily

[Previous](CommissionMonthly.md) | [Next](AgentMonthly.md)

# IMTDaily::AgentDaily

Get the size of agent [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged for a client's trade operations for a day from a daily report.

C++
    
    
    double  IMTDaily::AgentDaily()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.AgentDaily()

### Return Value

The size of agent commissions charged for a client's trade operations for a day, from a daily report.

# IMTDaily::AgentDaily

Set the size of agent [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) for a client's trade operations for a day in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::AgentDaily(
       const double  agent      // Agent commissions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.AgentDaily(
       double        agent      // Agent commissions
       )

### Parameters

**agent**  
[in] The size of agent commissions for a client's trade operations for a day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
