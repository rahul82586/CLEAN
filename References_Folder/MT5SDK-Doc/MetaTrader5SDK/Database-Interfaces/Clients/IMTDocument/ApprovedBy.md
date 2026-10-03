[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / ApprovedBy

[Previous](ApprovedDate.md) | [Next](DateIssue.md)

# IMTDocument::ApprovedBy

Get the manager who approved/checked the document.

C++
    
    
    UINT64  IMTDocument::ApprovedBy()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDocument.ApprovedBy()

### Return Value

The login of the manager who approved the document.

# IMTDocument::ApprovedBy

Set the manager who approved/checked the document.

C++
    
    
    MTAPIRES  IMTDocument::ApprovedBy(
       const UINT64  manager   // Manager
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.ApprovedBy(
       ulong         manager   // Manager
       )

### Parameters

**manager**  
[in] The login of the manager who approved the document.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

[IMTConManager::Login](../../../Configuration-Interfaces/Managers/IMTConManager/Login.md) is used for the login.
