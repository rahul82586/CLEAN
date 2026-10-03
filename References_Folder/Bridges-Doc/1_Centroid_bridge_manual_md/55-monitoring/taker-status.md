[🏠 Document Start](..\README.md) / [Maker Status](README.md) / Taker Status

# Taker Status

Overview
The Taker Status component offers a live health assessment of all Pricing and Trading connections across all Takers. It serves as a
valuable tool for diagnosing and resolving connectivity issues between Takers and the Centroid Bridge.
The Taker Status is categorized into three sections:
Trading Status
Depth Feeding Status
Feeder Status
Trading Status FIX & MT5, MT4 Trading Connection Status
Depth Feeding Status FIX Clients only Pricing Connection Status
Feeder Status MT5 and MT4 Clients only Pricing Connection Status
Session Type Taker Type Connection Status
Taker The name of the Taker which could be set up as one session combining both Feeding and Trading or two separate
sessions for each, Feeding and Trading.
Status

Shows the Status of the connection.
* Enabled: If Taker is enabled from Taker section.
* Disabled: If Taker is disabled from Taker section.
STime Indicates whether the connection is within the defined time session.
* Within Time: If the connection is within the defined time session.
* Outside Time: If the connection is outside the defined time session.
Example: If Time Session is from Monday to Friday, then Saturday would show Outside Time.
Logged in Indicates whether the session is connected or not.
* Connected: If there is an established connection between the Taker and the Centroid Bridge.
Field Description

Feeder Status
The Feeder Status component oversees the status and health of feeders associated with Takers of MT4, MT5, or Centroid types,
presenting relevant statistics in real time. Moreover, it enables users to inspect all the symbols to which Takers are subscribed on a per
Taker basis.
Subscription List Check
To review the list of symbols to which Takers are subscribed:
1. Click on the "Subscription List" next to the desired Taker.
2. In the pop-up window displaying the list of all subscriptions, enter one or multiple values (comma-separated) into the search box. You
can input either the full symbol name or a part of it. The symbols matching the criteria will be highlighted in yellow.
* Disconnected: If there is no established connection between the Taker and the Centroid Bridge.
Received
Count
The number of messages received by the Centroid Bridge from the Taker.
Sent Count The number of messages sent by the Centroid Bridge to the Taker.
Taker The name of the Taker
IP The IP of the Server on which the feeder/ platform (MT4 or MT4) is installed
Last Ping The last Date and Time the Feeder was pinged successfully
Received
Count
The number of messages received in the Centroid Bridge from the Taker which mainly consist of subscription to
Symbols
Sent
Count
The number of messages sent by the Centroid Bridge to the Taker mainly the ticks pertaining to the quotes streamed into
the Taker via Taker Feeds
Subscripti
on List
Allows to check all the Symbols the Taker is subscribed to, by clicking the button next to the desired Taker
Field Description





