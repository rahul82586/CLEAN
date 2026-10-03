[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Current

[Previous](Unsubscribe.md) | [Next](Get.md)

# IMTGatewayAPI::TimeCurrent

Get the current trading time.

C++
    
    
    INT64  IMTGatewayAPI::TimeCurrent()

.NET
    
    
    long  CIMTGatewayAPI.TimeCurrent()

### Return Value

The current trading time of the platform - the number of seconds elapsed since 01.01.1970.

### Note

The method returns time taking into account the /timezone and /timecorrect parameters, which are passed [in a command line when the gateway/datafeed is started](../../../Exported-Functions/MTGatewayCreateLocal.md). 

  * When a gateway/datafeed is started by the history server, the values of the /timezone and /timecorrect parameters are set in accordance with time settings on the trade server ([IMTConTime](../../../../Configuration-Interfaces/Time/IMTCon.md)).
  * When a gateway/datafeed is started as a service (remote gateway), these parameters should be specified by the user. If these parameters are not set, IMTGatewayAPI::TimeCurrent will pass time in the UTC+0 time zone.


