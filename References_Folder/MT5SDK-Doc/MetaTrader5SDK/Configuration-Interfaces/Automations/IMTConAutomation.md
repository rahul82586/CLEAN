[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Automations](../Automations.md) / IMTConAutomation

[Previous](../Automations.md) | [Next](IMTConAutomation/Enumerations.md)

# IMTConAutomation

The IMTConAutomation class contains method for receiving end editing [automation tasks](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation):

Method | Purpose  
---|---  
[Release](IMTConAutomation/Release.md) | Delete the current object.  
[Assign](IMTConAutomation/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConAutomation/Clear.md) | Clear an object.  
[ID](IMTConAutomation/ID.md) | Get a unique configuration identifier.  
[ParentID](IMTConAutomation/ParentID.md) | Get the ID of the subdirectory in which the automation task is located.  
[ParentIDSet](IMTConAutomation/ParentIDSet.md) | Set an ID of the subdirectory in which the automation task is located.  
[Name](IMTConAutomation/Name.md) | Get and set the name of the automation task.  
[Trigger](IMTConAutomation/Trigger.md) | Get and set a trigger — an event in the platform, upon occurrence of which the automation task should be executed.  
[Flags](IMTConAutomation/Flags.md) | Get and set additional automation task settings.  
[TimeStart](IMTConAutomation/TimeStart.md) | Get and set the date and time on which the trigger check will be activated.  
[TimeExpire](IMTConAutomation/TimeExpire.md) | Get and set the date and time after which the trigger check will be disabled.  
[TimeWeekdays](IMTConAutomation/TimeWeekdays.md) | Get and set the days on which the task automation trigger is allowed.  
[TimeMonths](IMTConAutomation/TimeMonths.md) | Get and set the months in which the task automation trigger is allowed.  
[TimeMonthdays](IMTConAutomation/TimeMonthdays.md) | Get and set the days of the month on which the task automation trigger is allowed.  
[EventPauseMinutes](IMTConAutomation/EventPauseMinutes.md) | Get and set the number of minutes in the period of time for which the number of repetitions should be checked.>  
[EventPauseHours](IMTConAutomation/EventPauseHours.md) | Get and set the number of hours in the period of time for which the number of repetitions should be checked.>  
[EventPauseDays](IMTConAutomation/EventPauseDays.md) | Get and set the number of days in the period of time for which the number of repetitions should be checked.>  
[EventRepeats](IMTConAutomation/EventRepeats.md) | Get and set the maximum number of event repetitions.  
[ConditionAdd](IMTConAutomation/ConditionAdd.md) | Add an automation task triggering condition.  
[ConditionUpdate](IMTConAutomation/ConditionUpdate.md) | Edit an automation task triggering condition at the specified position.  
[ConditionDelete](IMTConAutomation/ConditionDelete.md) | Delete an automation task triggering condition at the specified position.  
[ConditionClear](IMTConAutomation/ConditionClear.md) | Clear the list of all automation task triggering conditions.  
[ConditionShift](IMTConAutomation/ConditionShift.md) | Move an automation task triggering condition in the list.  
[ConditionTotal](IMTConAutomation/ConditionTotal.md) | Get the number of conditions of an automation task trigger.  
[ConditionNext](IMTConAutomation/ConditionNext.md) | Get an automation task triggering condition by index.  
[ActionAdd](IMTConAutomation/ActionAdd.md) | Add an automation task action.  
[ActionUpdate](IMTConAutomation/ActionUpdate.md) | Edit an automation task action at the specified position.  
[ActionDelete](IMTConAutomation/ActionDelete.md) | Delete an automation task action at the specified position.  
[ActionClear](IMTConAutomation/ActionClear.md) | Clear the list of all automation task actions.  
[ActionShift](IMTConAutomation/ActionShift.md) | Move an automation task action in the list.  
[ActionTotal](IMTConAutomation/ActionTotal.md) | Get the number of actions in an automation task.  
[ActionNext](IMTConAutomation/ActionNext.md) | Get an automation task action by index.  
  
The IMTConAutomation class contains the following enumerations:

Enumeration | Description  
---|---  
[EnFlags (#enflags)](IMTConAutomation/Enumerations.md#enflags) | Automation task setup flags.  
[EnTriggers (#entriggers)](IMTConAutomation/Enumerations.md#entriggers) | Triggers — events in the platform upon the occurrence of which the automation task should be executed.  
[EnTriggerWeekdays (#entriggerweekdays)](IMTConAutomation/Enumerations.md#entriggerweekdays) | Days on which task triggers can fire.  
[EnTriggerMonths (#entriggermonths)](IMTConAutomation/Enumerations.md#entriggermonths) | Months in which task triggers can fire.  
[EnTriggerMonthDays (#entriggermonthdays)](IMTConAutomation/Enumerations.md#entriggermonthdays) | Days of the month on which task triggers can fire.
