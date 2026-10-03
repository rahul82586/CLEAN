[🏠 Document Start](..\README.md) / [Taker Execution Rules](README.md) / FAQ - Taker Module

# FAQ - Taker Module

FAQ
Is it possible to add a new Taker Connection from our end?
Do we need to provide the Taker IPs to the Centroid Team?
What is the process for providing connection details to the FIX Taker?
What does specifying an IP during the creation of the taker entail? Does mentioning the IP mean it is automatically whitelisted for the taker?
Can multiple takers be assigned within a single Taker Feed?
Encountering challenges when saving a new taker feed? What could be the reasons for the error?
How can we ensure that the TEM (whether existing or newly added) is fully configured for B Book, and vice versa?
What does 'Min Volume' signify, and how can it be reconfigured?
Taker
Kindly note that users can add FIX as the taker connection type on their end. For MT5 and MT4 connections, we recommend
contacting our support team via email: support@centroidsol.com or Skype/Slack .
We kindly request the IPs of the newly added takers, Whitelisting these IPs ensures a smooth connection between Taker and the
Centroid Bridge.
To share connection details with your FIX Taker, you can access the "Export FIX Config" option on the extreme right to download the
FIX Details. Kindly note that this feature is exclusively for FIX Takers only.
Mentioning the IP during taker creation is for reference only and doesn't automatically whitelist it. To whitelist IPs, please share them
with Centroid via dedicated group chat or send an email to support@centroidsol.com
Taker Feed
Indeed, it is possible to assign multiple takers within a single Taker Feed.
Consider the following possibilities for the error:
If you're encountering issues with an existing suffix, ensure you're not attempting to save the same set of suffix taker feed with the
same taker.
If you're uploading a file, we recommend double-checking the Excel format for any potential discrepancies.
Taker Execution Model
To confirm whether the TEM is set up as B Book or A Book, just check the B Book percentage configured on the TEM level:
0 indicates the TEM is configured as complete A Book.
100 indicates the TEM is configured as complete B Book.
Min volume represents the minimum volume accepted at the bridge level; anything below this threshold will be declined.
To reconfigure, simply adjust the volume, considering the contract size and your desired minimum volume:
Volume = Contract Size × Lot Size.

Why was a particular order booked as B Book, even when the TEM is configured as A Book?

If an order is booked as B Book despite the TEM being configured as A Book, you might review your TEM settings. Specifically, check
AMin and AStep configurations. If these criteria's aren't met, the order may be booked as B Book, disregarding the TEM B Book%
configuration.

