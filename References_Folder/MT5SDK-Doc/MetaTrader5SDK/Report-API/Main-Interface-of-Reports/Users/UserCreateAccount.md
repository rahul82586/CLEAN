[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Users](../Users.md) / UserCreateAccount

[Previous](UserCreate.md) | [Next](UserGet.md)

# IMTReportAPI::UserCreateAccount

Create an object of a client's trading account.
    
    
    IMTAccount*  IMTReportAPI::UserCreateAccount()

### Return Value

It returns a pointer to the created object that implements the [IMTAccount](../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTAccount::Release](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Release.md) method of this object.
