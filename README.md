# Global Entry Interivew Scheduler

Basically `python scheduler.py` scrapes the [TTP website](https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&returnUrl=ttp-external&service=up) to determine if there is any availability at a specified interview location. The script sends a push notification to your mobile device indicating whether there is availability or not. Uses Pushover because it has a one month free trial and only $5 for a permanent license (as of March 2025).

I don't have recommendations for automation yet (e.g. run daily at 8am), as that might vary based on machine operating system. Open to suggestions.

The push notification contains text like
```
Appointments Available!
Next Available Appointment: August 13, 2025
Accessed: 2025-03-09T16:28:45
Location: Boise Enrollment Center
https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&returnUrl=ttp-external&service=up
```

## Setup

0. On your machine, configure your python environment. The script requires `python<=3.10`, `selenium`, `webdriver-manager`, and `pushover`. Unfortunately, Pushover only works in `python<=3.10` due to dependence on `SafeConfigParser` (see below for conda tutorial).
2. On your mobile device, download the Pushover app and create a Pushover account.
3. On the Pushover website, login and create a new application to generate an API token.
4. On your machine, clone this repository somewhere and modify the `scheduler_config.ini` file with your user id and API token.

## Usage

1.  After setup, modify `scheduler_config.ini` with the desired location number. Although the location number is not visible on the TTP website, you can find the location number by inspecting the web element of the location (e.g. the location number of Boise Enrollment Center is 120).

## Example Config File

The config file `scheduler_config.ini` should look something like
```
[pushover]
user_key = <your Pushover user id>
app_key = <your API token>
[location]
location=120
```

## Setting up environment using conda

If you have anaconda installed, you can just create a new environment

`conda create -n scheduler python=3.10 selenium webdriver-manager -c conda-forge`

Then run `conda activate scheduler` and then `conda pip install pushover`
