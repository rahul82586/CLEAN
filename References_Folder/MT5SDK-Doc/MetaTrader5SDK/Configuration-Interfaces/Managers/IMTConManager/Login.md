[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / Login

[Previous](Clear.md) | [Next](Mailbox.md)

# IMTConManager::Login

Get the login of a manager.

C++
    
    
    UINT64  IMTConManager::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConManager.Login()

Python (Manager API)
    
    
    MTConManager.Login

### Return Value

The login of a manager.

# IMTConManager::Login

Set the login of a manager.

C++
    
    
    MTAPIRES  IMTConManager::Login(
       const UINT64  login      // Manager's login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.Login(
       ulong         login      // Manager's login
       )

Python (Manager API)
    
    
    MTConManager.Login

### Parameters

**login**  
[in] The login of a manager.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The login must first be created in the [accounts](../../../Database-Interfaces/Users.md) section. Such an account must be included in the [group](../../Groups.md) of managers or administrators.
