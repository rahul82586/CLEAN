[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerStart

[Previous](DealerExecutionCreate.md) | [Next](DealerStop.md)

# IMTGatewayAPI::DealerStart

Gateway connection to the trading platform as a dealer.

C++
    
    
    MTAPIRES  IMTGatewayAPI::DealerStart(
       const UINT  flags      // Connection flags
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.DealerStart(
       uint        flags      // Connection flags
       )

### Parameters

**flags**  
[in] The flags describing additional options for connection as a dealer. To pass the flags, theIMTGatewayAPI::EnDealerRequestFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After this method execution the trade requests queue will be downloaded to the application and [trading requests events](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) will start coming (IMTRequestSink::OnRequestAdd, IMTRequestSink::OnRequestUpdate and IMTRequestSink::OnRequestDelete).
