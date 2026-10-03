[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Trade Server](../Trade-Server.md) / Mail Templates

[Previous](Structure-of-Directories-and-Files.md) | [Next](Daily-Reports.md)

<a id="mail-templates"></a>
# Mail Templates (#mail-templates)

Several types of emails that are automatically sent to clients are implemented in the the MetaTrader 5 platform:

  * Welcoming email at account opening;
  * Email requesting the certificate confirmation;
  * Daily report on trade activity;
  * Monthly report on trade activity.



  * All templates must be of the Unicode format (UTF-16/UCS-2 Little Endian). 


  * In order to start using a new template, the main trade server must be restarted.

  
---  
  
<a id="greeting"></a>
## Welcoming Emails (#greeting)

Welcome messages are sent to clients through the internal mail system when an account is opened. It does not matter how the account is opened: by the trader via the client terminal or by the broker via the Manager/Administrator terminal. The welcome email contains the account number and password, as well as general information about the MetaTrader 5 platform.

Welcome email templates are located in the following [directory (#templates)](Structure-of-Directories-and-Files.md#templates):

  * Trader server directory\templates\greeting\default\*.htm — default templates used for groups;
  * Trader server directory\templates\greeting\custom folder*.htm — templates of emails that can be sent only to separate groups with account of their settings;
  * Trader server directory\templates\greeting\preliminary\*.htm — templates of emails that are sent when a [preliminary account (#preliminary)](../../Platform-Setup/Groups/Group-Types.md#preliminary) is opened from the client terminal.



> An unlimited number of folders with special templates can be create. The name of the folder with templates that will be used for a group are specified in the "Company" tab in its [settings (#templates-folder)](../../Platform-Setup/Groups/Group-Settings.md#templates-folder).

<a id="certificate"></a>
## Certificate Confirmation Email (#certificate)

These letters are sent if the [extended authorization (#authorization)](../../Platform-Setup/Groups/Group-Settings.md#authorization) and [certificate confirmation (#confirm)](../../MetaTrader-5-Administrator/Getting-Started/Connect-to-Server/Extended-Authorization.md#confirm) mode is enabled for this group. Such an email contains information on how to confirm a certificate. Templates of such emails are stored in the following [directory (#templates)](Structure-of-Directories-and-Files.md#templates):

  * Trader server directory\templates\certificate\default\*.htm — default templates used for groups;
  * Trader server directory\templates\certificate\custom folder*.htm — templates of emails that are sent only to separate groups with account of their settings.



<a id="confirm"></a>
## Phone and Email Verification (#confirm)

These emails\messages are sent to [verify phone numbers and emails (#confirmation)](../../Platform-Setup/Accounts/Account-Allocation-Settings.md#confirmation), specified during registration of demo and preliminary accounts from client terminals.

  * Trader server directory\templates\verify_email\default\*.htm — email templates as HTM files.
  * Trader server directory\templates\verify_phone\default\*.htm — SMS templates as text files. Do not use too long messages. If the allowed length is exceeded (depending on the provider), a message may be cropped or split into multiple SMS.



The <!--CONFIRMATION_CODE--> macro is used for confirmation emails. This code adds the generated confirmation code to the text.

Templates from the "default" folder are used on default for all groups. If you need to use custom templates for a specific group, create another folder in the same directory and place the template files to it. Then specify the folder name in the [group settings (#templates-folder)](../../Platform-Setup/Groups/Group-Settings.md#templates-folder).

<a id="daily"></a>
## Daily Report on Trade Activity (#daily)

Daily reports on trade activity of clients are sent if the "Send daily statements by email" option is enabled in the [group settings (#reports)](../../Platform-Setup/Groups/Group-Settings.md#reports). Templates of such emails are stored in the following:

  * Trader server directory\templates\confirmation\default\*.htm — default templates used for groups;
  * Trader server directory\templates\confirmation\custom folder*.htm — templates of reports that are sent only to separate groups with account of their settings.



<a id="monthly"></a>
## Monthly Report on Trade Activity (#monthly)

Monthly reports on trade activity of clients are sent if the "Send daily statements by email" option is enabled in the [group settings (#reports)](../../Platform-Setup/Groups/Group-Settings.md#reports). Templates of such emails are stored in the following:

  * Trader server directory\templates\statement\default\*.htm — default templates used for groups;
  * Trader server directory\templates\statement\custom folder*.htm — templates of reports that are sent only to separate groups with account of their settings.



<a id="multilanguage"></a>
## Email templates in different languages (#multilanguage)

All template files should be named according to the language they are written in. A file name is used by the platform to determine which users the template is to be applied to. The user's language is defined in the [account settings (#personal)](../../Platform-Setup/Accounts/Editing-Account.md#personal).

Languages are specified in the format standard for the family of Windows operating systems, though without the specification of regional dialect specifics. E.g. English.htm, Russian.htm and so on. The only exceptions are Chinese language templates. In case of simplified Chinese, a template should be named chinese.htm, while in case of traditional Chinese, it is named chinese_traditional.htm.

If no template was found for the language specified in the account, the default.htm template is used. If a separate folder is specified for a group, the default template is first searched for in this folder, and if it is not found an email according to the default.htm template located in the "Default" folder is sent.

<a id="the-format-of-files"></a>
## The Format of Files (#the-format-of-files)

A template file can contain a plain text, HTML tags, as well as CSS design elements. To insert images, set them on your web server and specify the appropriate links in <img src="URL">. The web server must operate using the HTTPS protocol. Images with URLs starting with http:// will not be displayed.

Besides, the templates can be equipped with special macros for inserting various data depending on an account an email is sent to.

  * Common macros
  * <!--ACCOUNT--> — account number.
  * <!--LOGIN--> — account number.
  * <!--GROUP--> — user group.
  * <!--PASSWORD--> — account master password.
  * <!--INVESTOR--> — account investor password.
  * <!--NAME--> — user first name (obsolete macro).
  * <!--USERNAME--> — user first name (obsolete macro).
  * <!--FIRST_NAME--> — user first name.
  * <!--LAST_NAME--> — user last name.
  * <!--MIDDLE_NAME--> — user middle name.
  * <!--COUNTRY--> — country of residence.
  * <!--CITY--> — city of residence.
  * <!--STATE--> — state (region) of residence.
  * <!--ZIPCODE--> — zip code.
  * <!--ADDRESS--> — residential address.
  * <!--PHONE--> — phone number.
  * <!--EMAIL--> — email address.
  * <!--COMMENT--> — account comment.
  * <!--ID--> — ID.
  * <!--STATUS--> — residency status.
  * <!--PHONEPASS--> — phone password.
  * <!--AGENT--> — agent account associated with the user.
  * <!--CURRENCY--> — account deposit currency.
  * <!--COMPANY--> — [company name (#company-name)](../../Platform-Setup/Groups/Group-Settings.md#company-name) from the account group settings.
  * <!--LEVERAGE--> — recipient's current leverage.



<a id="daily-and-monthly-report-macros"></a>
### Daily and monthly report macros (#daily-and-monthly-report-macros)

  * <!--DATE--> — date the report is generated for, YYYY.MM.DD.
  * <!--TIME--> — time the report is generated for, HH::MM:SS.
  * <!--FULLTIME--> — date and time the report is generated for, YYYY.MM.DD HH::MM:SS.
  * <!--BALANCE--> — balance at the time of the report generation.
  * <!--CREDIT--> — credit funds at the time of the report generation.
  * <!--INTERESTRATE--> — client's annual interest rate.
  * <!--COMMISSION_DAILY--> — amount of standard commissions charged from a client for the day the report is generated for.
  * <!--COMMISSION_MONTHLY--> — amount of standard commissions charged from a client for the month the monthly report is generated for (or for the current month in case of a daily report).
  * <!--AGENT_DAILY--> — agent commissions charged from a client for the day the report is generated for.
  * <!--AGENT_MONTHLY--> — agent commissions charged from client's operations for the month the monthly report is generated for (or for the current month in case of a daily report).
  * <!--PREV_BALANCE_DAILY--> — client balance at the end of the previous trading day.
  * <!--PREV_BALANCE_MONTHLY--> — client balance at the end of the previous month.
  * <!--PREV_EQUITY_DAILY--> — client equity at the end of the previous trading day.
  * <!--PREV_EQUITY_MONTHLY--> — client equity at the end of the previous month.
  * <!--PREV_DATE--> — the date of the last but one closure of the trading day.
  * <!--PREV_TIME--> — the time of the last but one closure of the trading day.
  * <!--PREV_FULLTIME--> — the date and time of the last but one closure of the trading day.
  * <!--MARGIN--> — money required to cover open positions as of the end of the day/month.
  * <!--MARGIN_FREE--> — amount of free margin volume as of the end of the day/month.
  * <!--MARGIN_LEVEL--> — margin level as of the end of the day/month.
  * <!--FLOATING_PROFIT--> — floating profit/loss on all open positions at the time of the report generation.
  * <!--FLOATING_STORAGE--> — size of swaps charged for client's positions for a day, but not yet reflected in the balance.
  * <!--FLOATING_COMMISSION--> — floating client commission blocked on the account but not yet reflected in the balance at the time of the report generation.
  * <!--FLOATING_EQUITY--> — client equity volume at the time of the report generation.
  * <!--FLOATING_PL--> — total client's floating profit/loss at the time of the report generation. Calculated as <!--FLOATING_PROFIT--> \+ <!--FLOATING_STORAGE--> \+ <!--FLOATING_COMMISSION-->.
  * <!--FLOATING_LIABILITIES--> — amount of client liabilities at the time of report generation. It is only used for the [Exchange risk management model (#risk)](../../Platform-Setup/Groups/Group-Settings.md#risk).
  * <!--FLOATING_ASSETS--> — amount of client assets at the time of report generation. It is only used for the [Exchange risk management model (#risk)](../../Platform-Setup/Groups/Group-Settings.md#risk).
  * <!--CLOSED_PROFIT--> — total closed profit/loss at all deals per day/month.
  * <!--CLOSED_STORAGE--> — size of swaps charged for a client's positions for a day/month.
  * <!--CLOSED_DEPOSIT--> — total funds deposited/withdrawn from the account per day/month.
  * <!--CLOSED_CREDIT--> — credit funds deposited/withdrawn from the account per day/month.
  * <!--CLOSED_CHARGE--> — other depositions/withdrawals from the client's balance per day/month.
  * <!--CLOSED_CORRECTION--> — corrective balance operations performed on the client's account per day/month.
  * <!--CLOSED_BONUS--> — bonus funds deposited/withdrawn from the account per day/month.
  * <!--CLOSED_COMMISSION_INSTANT--> — standard commissions withdrawn from a client's account per day/month instantly (during a trade).
  * <!--CLOSED_COMMISSION_ROUND--> — commission by orders and positions accumulated during a day/month. Depending on the settings (specified for the group in the administrator terminal), preliminary commission calculation is performed during a day/month and the appropriate funds are blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by the balance operation.
  * <!--CLOSED_FEE--> — total fees charged from the client for the day/month.
  * <!--CLOSED_AGENT--> — agent commissions charged from the client for the day the report is generated for.
  * <!--CLOSED_INTEREST--> — annual interest rate accruals per day/month the report is generated for.
  * <!--CLOSED_DIVIDEND--> — dividends received by the client per day/month the report is generated for.
  * <!--CLOSED_TAX--> — taxes charged per day/month the report is generated for.
  * <!--CLOSED_PL--> — total profit/loss at a client's account per day/month the report is generated for. Calculated as <!--CLOSED_PROFIT--> \+ <!--CLOSED_STORAGE--> \+ <!--CLOSED_COMMISSION_INSTANT-->.
  * <!--CLOSED_ADDITIONAL--> — financial result of other transactions conducted on the account for the day/month the report is generated for. These are additional charges, corrections, bonuses, agent commissions, annual interests, dividends and taxes
  * <!--CLOSED_TOTAL--> — total financial result of the client's account for the day/month the report is generated for. Calculated as the sum of all the above values with the <!--CLOSED_*--> prefix apart from <!--CLOSED_PL--> and <!--CLOSED_ADDITIONAL-->.
  * <!--CLOSED_SO_COMPENSATION--> — the sum of balance operations connected with [the negative balance compensation (#compensate)](../../Platform-Setup/Groups/Group-Settings.md#compensate) after Stop Out.
  * <!--CLOSED_COST--> — the total amount of costs for all deals for the day/month for which the report is generated. The value calculation does not depend on [group settings (#deal-cost)](../../Platform-Setup/Groups/Group-Settings.md#deal-cost). If a macro is included in a report template, its value will be calculated and substituted.
  * <!--PREV_EQUITY_DIFF_PERC_DAILY--> — a change in equity as compared to the previous day value. Indicated as a percentage.
  * <!--PREV_EQUITY_DIFF_PERC_MONTHLY--> — a change in equity as compared to the previous month value. Indicated as a percentage.



<a id="macros-of-trading-operations"></a>
### Macros of Trading Operations (#macros-of-trading-operations)

Daily reports include blocks of trading operations performed by a client during a day/month. Each of these blocks begins with a macro corresponding to the operation type:

  * <!--MQTABLE=Closed Orders--> — closed orders.
  * <!--MQTABLE=Closed Deals--> — executed deals.
  * <!--MQTABLE=Positions--> — current open positions.
  * <!--MQTABLE=Orders--> — current open orders.



Each of these blocks ends with the <!--MQTABLE--> macro. Information about trading operations is displayed using macros inside the blocks. Depending on the block in which a macro is contained, it substitutes information about the appropriate operation type, i.e. order, deal or positions.

  * <!--Ticket--> — the ticket of a trading operation.
  * <!--Type--> — the type of a trading operation (buy, sell or a pending order).
  * <!--Size--> — the volume of a trading operation. The initial and filled volume is additionally displayed for orders.
  * <!--Item--> — the name of a trading instrument.
  * <!--ISIN--> — International Securities Identification Number (ISIN).
  * <!--Price--> — the price at which a trading operation was executed.
  * <!--SL--> — the Stop Loss level.
  * <!--TP--> — the Take Profit level.
  * <!--Open Time--> — operation time.
  * <!--Close Time--> — order or position closing time.
  * <!--State--> — order status (filled, rejected, canceled).
  * <!--Comment--> — a comment on the operation.
  * <!--Entry--> — trade direction (in, out, in/out).
  * <!--Commission--> — commission charged for the operation.
  * <!--Fee--> — the amount of fees for the operation.
  * <!--Swap--> — operation swap.
  * <!--Cost--> — the amount of costs incurred when performing deals relative to the current mid-point spread cost. The value calculation does not depend on [group settings (#deal-cost)](../../Platform-Setup/Groups/Group-Settings.md#deal-cost). If a macro is included in a report template, its value will be calculated and substituted.
  * <!--Profit--> — profit received from the operation.
  * <!--Market--> — the market price of a trading instrument at the time of report generation.
  * <!--Color--> — a macro for alternating the background color of even and odd rows (a row with a white background, the next one has a gray background, etc).


