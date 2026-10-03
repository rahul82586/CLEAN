[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Common](../Common.md) / IMTConAccountAllocation

[Previous](IMTConCommon/IMTCon-AccountAllocationNext.md) | [Next](IMTConAccountAllocation/Enumerations.md)

# IMTConAccountAllocation

The IMTConAccountAllocation class contains methods for working with [account allocation settings](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_accounts/account_allocation_groups). Each IMTConAccountAllocation object describes settings for a particular account group.

Method | Purpose  
---|---  
[Release](IMTConAccountAllocation/Release.md) | Delete the current object.  
[Assign](IMTConAccountAllocation/Assign.md) | Assign the passed object to the current one.  
[Clear](IMTConAccountAllocation/Clear.md) | Clear an object.  
[Group](IMTConAccountAllocation/Group.md) | Get and set the group in which the accounts requested through terminals will be opened.  
[Description](IMTConAccountAllocation/Description.md) | Get and set the group description displayed in the "Account type" field in client terminals.  
[Flags](IMTConAccountAllocation/Flags.md) | Get and set additional account allocation settings for the group.  
[Leverages](IMTConAccountAllocation/Leverages.md) | Get and set the list of available leverage options which can be selected when opening an account in this group.  
[Countries](IMTConAccountAllocation/Countries.md) | Get and set the list of countries in which it will be possible to open an account in this group.  
[ConfirmationEmail](IMTConAccountAllocation/ConfirmationEmail.md) | Get and set the mail server which will be used for email confirmations when opening accounts in this group.  
[AccountAgreementAdd](IMTConAccountAllocation/AccountAgreementAdd.md) | Add an agreement to the account allocation configuration.  
[AccountAgreementUpdate](IMTConAccountAllocation/AccountAgreementUpdate.md) | Edit an agreement in the account allocation configuration.  
[AccountAgreementDelete](IMTConAccountAllocation/AccountAgreementDelete.md) | Remove an agreement from the account allocation configuration.  
[AccountAgreementClear](IMTConAccountAllocation/AccountAgreementClear.md) | Clear the list of agreements in the account allocation configuration.  
[AccountAgreementShift](IMTConAccountAllocation/AccountAgreementShift.md) | Move an agreement in the account allocation configuration.  
[AccountAgreementTotal](IMTConAccountAllocation/AccountAgreementTotal.md) | Get the number of agreements in the account allocation configuration.  
[AccountAgreementNext](IMTConAccountAllocation/AccountAgreementNext.md) | Get agreement by index.  
  
The IMTConAccountAgreement class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnFlags (#enflags)](IMTConAccountAllocation/Enumerations.md#enflags) | Additional agreement settings.
