[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon Action

[Previous](IMTCon-Clear.md) | [Next](IMTCon-From.md)

# IMTConFirewall::Action

Get the type of actions undertaken in accordance with the firewall rule.

C++
    
    
    UINT  IMTConFirewall::Action()  const

.NET (Gateway/Manager API)
    
    
    EnAction  CIMTConFirewall.Action()

Python (Manager API)
    
    
    MTConFirewall.Action

### Return Value

One of the value of the [IMTConFirewall::EnAction (#enaction)](IMTCon-Enumerations.md#enaction) enumeration.

# IMTConFirewall::Action

Sets the type of actions performed in accordance with the firewall rule.

C++
    
    
    MTAPIRES  IMTConFirewall::Action(
       const UINT  action      // Type of action
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFirewall.Action(
       EnAction    action      // Type of action
       )

Python (Manager API)
    
    
    MTConFirewall.Action

### Parameters

**action**  
[in] The type of action. TheIMTConFirewall::EnActionenumeration is used to pass the action type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
