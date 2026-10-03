[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Login

[Previous](ID.md) | [Next](Subscription.md)

# IMTSubscription::Login

Get the login of the client to whom the subscription belongs.

C++
    
    
    UINT64  IMTSubscription::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSubscription.Login()

### Return Value

The login of the client ([IMTUser::Login](../../Users/IMTUser/Login.md)) to whom the subscription belongs.

# IMTSubscription::Login

Set the login of the client to whom the subscription belongs.

C++
    
    
    MTAPIRES  IMTSubscription::Login(
       const UINT64  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.Login(
       ulong         login      // Login
       )

### Parameters

**login**  
[in] The login of the client (IMTUser::Login) to whom the subscription belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
