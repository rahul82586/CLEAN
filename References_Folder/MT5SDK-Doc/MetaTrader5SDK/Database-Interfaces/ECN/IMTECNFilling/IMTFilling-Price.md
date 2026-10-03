[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Price

[Previous](IMTFilling-VolumeCurrentExt.md) | [Next](IMTFilling-Digits.md)

# IMTECNFilling::Price

Get the price of the order created in the ECN for the filling of the client order.

C++
    
    
    double  IMTECNFilling::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNFilling.Price()

### Return Value

Order price in the ECN.

# IMTECNFilling::Price

Set the price of the order created in the ECN for the filling of the client order.

C++
    
    
    MTAPIRES  IMTECNFilling::Price(
       const double  price      // order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Price(
       double        price      // order price
       )

### Parameters

**price**  
[in] Order price in the ECN.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
