[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / InterestRate

[Previous](LeadCampaign.md) | [Next](CommissionDaily.md)

# IMTUser::InterestRate

Get the amount accrued for the current month calculated based on the annual interest rate.

C++
    
    
    double  IMTUser::InterestRate()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTUser.InterestRate()

### Return Value

The amount accrued for the current month calculated based on the annual interest rate.

### Note

The interest is calculated every day, but the amount is accrued once at the end of the month.
