[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Funds and ETF](../Funds-and-ETF.md) / FundInvestorCreate

[Previous](FundAccountCreate.md) | [Next](FundTotal.md)

# IMTReportAPI::FundInvestorCreate

Create a fund investor object.
    
    
    IMTConFundInvestor*  IMTReportAPI::FundInvestorCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConFundInvestor](../../../../Configuration-Interfaces/Funds-and-ETF/IMTConFundInvestor.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConFundInvestor::Release](../../../../Configuration-Interfaces/Funds-and-ETF/IMTConFundInvestor/Release.md) method of this object.
