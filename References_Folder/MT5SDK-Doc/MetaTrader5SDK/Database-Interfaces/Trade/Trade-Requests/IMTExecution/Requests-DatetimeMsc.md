[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DatetimeMsc

[Previous](Requests-Datetime.md) | [Next](Requests-Login.md)

# IMTExecution::DatetimeMsc

Get the time of a trade execution occurrence in an external trading system in milliseconds.

C++
    
    
    INT64  IMTExecution::DatetimeMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTExecution.DatetimeMsc()

### Return Value

The time of a trade execution occurrence in an external trading system. The date is specified in milliseconds that have elapsed since 01.01.1970.

# IMTExecution::DatetimeMsc

Set the time of a trade execution occurrence in an external trading system in milliseconds.

C++
    
    
    MTAPIRES  IMTExecution::DatetimeMsc(
       const INT64  datetime      // Trade execution time in ms
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DatetimeMsc(
       long         datetime      // Trade execution time in ms
       )

### Parameters

**datetime**  
[in] The time of a trade execution occurrence in an external trading system. The date is specified in milliseconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the value [IMTExecution::Datetime](Requests-Datetime.md) will be filled automatically.

Type of Trade Execution | Action  
---|---  
TE_ORDER_NEW | Setting the time of placement of an order in an external system. The following fields are filled with the IMTExecution::DatetimeMsc value:

  * [IMTOrder::TimeSetup](../../Orders/IMTOrder/TimeSetup.md)
  * [IMTORder::TimeSetupMsc](../../Orders/IMTOrder/TimeSetupMsc.md)

  
TE_ORDER_FILL | Setting the time of filling of an order in an external system as well as setting the time of execution of the corresponding deal. The following fields are filled with the IMTExecution::DatetimeMsc value:

  * [IMTOrder::TimeDone](../../Orders/IMTOrder/TimeDone.md)
  * [IMTOrder::TimeDoneMsc](../../Orders/IMTOrder/TimeDoneMsc.md)
  * IMTDeal::Time
  * IMTDeal::TimeMsc

  
TE_ORDER_MODIFY | Setting a new time of placement of an order. Such algorithm is implemented due to specific procedure of modification of orders in most of the external systems: an order is modified by deleting the old one and creating a new one. The following fields are filled with the IMTExecution::DatetimeMsc value:

  * [IMTOrder::TimeSetup](../../Orders/IMTOrder/TimeSetup.md)
  * [IMTORder::TimeSetupMsc](../../Orders/IMTOrder/TimeSetupMsc.md)

  
TE_ORDER_CANCEL | Setting a new time of execution of an order. The following fields are filled with the IMTExecution::DatetimeMsc value:

  * [IMTOrder::TimeDone](../../Orders/IMTOrder/TimeDone.md)
  * [IMTOrder::TimeDoneMsc](../../Orders/IMTOrder/TimeDoneMsc.md)


