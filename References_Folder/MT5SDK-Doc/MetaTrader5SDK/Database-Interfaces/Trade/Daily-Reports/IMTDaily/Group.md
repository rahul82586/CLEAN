[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Group

[Previous](Name.md) | [Next](Currency.md)

# IMTDaily::Group

Get the [group](../../../../Configuration-Interfaces/Groups/IMTConGroup.md) of a client in a daily report.

C++
    
    
    LPCWSTR  IMTDaily::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDaily.Group()

### Return Value

If successful, it returns a pointer to a string with the client group in a daily report. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDaily](../IMTDaily.md) object.

# IMTDaily::Group

Set the [group](../../../../Configuration-Interfaces/Groups/IMTConGroup.md) of a client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Group(
       LPCWSTR  group      // Group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Group(
       string   group      // Group
       )

### Parameters

**group**  
[in] Client group in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The [IMTConGroup::Group](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md) value is used as the group name.
