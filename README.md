# Global Entry Interivew Scheduler

Scrapes the [TTP website](https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&returnUrl=ttp-external&service=up) to determine if the desired location has any availability. Then sends a push notification to mobile device indicating whether there is availability or not. Uses Pushover because it has a one month free trial and only $5 for a permanent license (as of March 2025).

## Setup

0. On your machine, install `python<=3.10`, `selenium`, `webdriver-manager`, and `pushover`. Unfortunately, Pushover only works in `python<=3.10` due to dependence on `SafeConfigParser`
1. On your mobile device, download the Pushover app on mobile device and create a Pushover account
2. On the Pushover website, login and create a new application to generate an API token
3. On your machine, modify `scheduler_config.ini` file with your user id and API token

## Usage

1.  After setup, modify `scheduler_config.ini` with the desired location number. Although the location number is not visible on the TTP website, you can find the location number by inspecting the web element of the location (e.g. Boise Enrollment Center is 120).

## Example Config File

The config file `scheduler_config.ini` should look something like
```
[pushover]
user_key = <your Pushover user id>
app_key = <your API token>
[location]
location=120
```
