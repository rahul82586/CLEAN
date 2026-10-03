[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Funds and ETF](../Funds-and-ETF.md) / FundAccountCreate

[Previous](FundCreate.md) | [Next](FundInvestorCreate.md)

# IMTReportAPI::FundAccountCreate

Create a fund manager object.
    
    
    IMTConFundAccount*  IMTReportAPI::FundAccountCreate()

### Return Value

Returns a pointer to the created object implementing the [IMTConFundAccount](../../../../Configuration-Interfaces/Funds-and-ETF/IMTConFundAccount.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConFundAccount::Release](../../../../Configuration-Interfaces/Funds-and-ETF/IMTConFundAccount/Release.md) method of this object.
