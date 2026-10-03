[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Users](../Users.md) / UserAccountGet

[Previous](UserLogins.md) | [Next](UserSelect.md)

# IMTReportAPI::UserAccountGet

Obtaining a client's trading account by a login.
    
    
    MTAPIRES  IMTReportAPI::UserAccountGet(
       const UINT64  login,       // Client login
       IMTAccount*   account      // An object of a trading account
       )

### Parameters

**login**  
[in] The login of a client.

**account**  
[out] An object of a client trading account. The account object must be created using theIMTReportAPI::UserCreateAccountmethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

To get the trade accounts, generation of an appropriate snapshot must be turned on in a report ([MTReportInfor::SNAPSHOT_ACCOUNTS (#ensnapshots)](../../../Structures/MTReportInfo.md#ensnapshots) or [MTReportInfo::SNAPSHOT_ACCOUNTS_FULL (#ensnapshots)](../../../Structures/MTReportInfo.md#ensnapshots)).
