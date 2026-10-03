[🏠 Document Start](..\README.md) / [Monitoring](README.md) / Logs

# Logs

Overview
The Logs feature lets you check detailed records of the Centroid Bridge. These logs hold important information for investigating
connectivity, pricing, and trading problems, as well as updates to configurations and other relevant details. You can see current logs in real
time, while past logs are compressed and saved in the Centroid Bridge at regular intervals.
Log Types
In-Depth Explanation of All Log Types
1. Makers
Where to Find the Makers Log: Path → Monitoring → Logs → Makers → Two folders available “marketdata” for pricing “trading” for
trading logs respectively.
Makers Maker logs encompass all the trading and pricing details between your Centroid Bridge and the
corresponding Maker.
Takers Taker logs encompass all the trading and pricing details between your Centroid Bridge and the corresponding
Taker.
Feeder The Feeder contains all the ticks forwarded to your taker, providing real-time ticks specifically tailored for
MT4/MT5 takers only.
Trade Statement If you have Risk Accounts set up in your Centroid Bridge, a statement is generated and stored here at the
end of each day. This statement includes all the transactions conducted throughout the day along with
additional details.
Downloads In addition to the Online Manual, you can conveniently find the most recent versions for both GW and Feeder
in the download section.
System The system log compiles all the details of activities carried out at the bridge level. This includes recording any
changes made to any component on the bridge.
Log type Description

formatted as YY/MM/DD Hours/Minutes/Seconds. For reading the downloaded logs, you can utilize FIX Parser. Follow these steps:
Download the log file, locate the specific order or logline, and copy-paste it into the provided link.
What Are the Logs About: The Maker logs provide valuable insights into whether you are receiving prices from a specific maker. They
also offer information on the reasons for rejection, providing clarity on whether your trade was successful, partially filled, or rejected. In the
case of rejection, the logs specify the reasons behind the rejection, enhancing your understanding of the trading process.
Note: Centroid Bridge stores “Pricing or Market Data” internally for a maximum period of 7 days.


2. Takers
Where to Find the Takers Log: Path → Monitoring → Logs → Takers → Two separate folders available “MD_Taker_Name” for pricing
and “TD_Taker_Name” for trading logs respectively.
Note: For Taker type MT4/MT5 Centroid bridge does not store the ticks in the “marketdata” folder.
How to Download/Read the Logs: To ensure you download the accurate log file, review the timestamp for each file, where the time is
formatted as YY/MM/DD Hours/Minutes/Seconds. For reading the downloaded logs, you can utilize FIX Parser. Follow these steps:
Download the log file, locate the specific order or logline, and copy-paste it into the provided link.
What Are the Logs About: As mentioned earlier, pricing data is not stored for MT4/MT5 taker types. However, through FIX connections,
both Pricing and Trading logs are available. The Trading log is particularly useful for verifying the orders received by the bridge from your
Taker. It provides details on whether the order was filled, rejected, or partially filled at the bridge level, and any corresponding out
messages sent back to your Taker.
Note: For taker connection type “DropCopy” there will be only one folder available as “Trading” Given that it exclusively encompasses a
trading session, the naming convention follows the format DC_TakerName.
3. Feeder
Where to Find the Feeder Log: Path → Monitoring → Logs → Feeder, This log file is specifically designated for your Taker types MT4
and MT5. If enabled on the backend, it will commence storing pricing data for MT4/5 takers. In the presence of both taker types (MT4 and
MT5), the log file consolidates pricing data, and you can distinguish them by entering your Taker Name after downloading the file.
Note: To enable this functionality, it must be activated at the configuration level of your Centroid Bridge. This process can be facilitated
from the support side.


4. Trade Statements
Where to Find the Statement: Path → Monitoring → Logs → Trade Statements
What Is the Statement About: Trade Statements are automatically generated daily and saved as HTML files at the close of each trading
day, provided you have Risk Accounts within your Centroid Bridge. To view a statement, you need to download it to your local machine and
then open it as an HTML file. The Trade Statement adheres to the naming convention: YY/MM/DD_RiskAccountName.html.


5. System
Where to Find the System Logs: Path → Monitoring → Logs → System
What Are the Logs About: The System Log encompasses all changes made at the bridge level, recording any addition or modification to
its components. In addition to these changes, it also keeps a record of all trades, regardless of whether they belong to the A book or B
book. You have the option to download the system logs, and you can read them using a simple text editor like Notepad.
System logs can be categorized into different types, classified as follows:
[I] → Info
[W] → Warning
[E] → Error
[D] → Debug
[T] → Trace
Note: The System Log is typically stored as one log file for an entire day.




