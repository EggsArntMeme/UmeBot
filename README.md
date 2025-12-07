# UmeBot
This is a work in progress bot to automate playing Umamusume

## Current Status
Currently in the data collection aspect.
Specifically on the collection of the stat increases on the training screen

### Next Goal
- Debugging Stat Data Collection

### Current Issues
- Number 1 fails to get recognized
- Number 7 sometimes fails to get detected
- Guts training sometimes obscures Stat bonus, causing for it to miss data


## Road Map
- Data Collection
  - Collect Training Stat Increases   <- (currently on this)
  - Collect Energy
  - Collect Friendship Level (and which friends are on what training)
  - Collect Mood Level
- Data Processing
   - Create Json for Prefrences
   - Determine what makes a "good" choice
   - Allow for data to be inserted to then determine a choice
- Automation
  - Finding timings and locations of buttons
  - Creating the auto clicks 
- GUI
  - Create a handy dandy GUI for users to use to download and easily use the UmeBot
