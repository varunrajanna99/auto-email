# Auto Email

A simple python script that checks for new emails and sends out automatic emails saying thanks

## Getting Started

Clone or download the repository and create a .env file in the same directory where the script is located, the script reads three variables from the env file

```env
EMAIL=<Your email address>
PASSWORD=<Your email password>
PORT=<gmail port for poplib>
```

### Prerequisites

The things you need before running the script.

* You need to have python with version greater than 3.7 installed
* You need to install `dotenv` using the below command

```
pip install python-dotenv
```

## Usage

Once everything is setup execute the script using the below command 

```
python3 auto_email.py
```

The script will check for new emails and send a email of whatever text you've used on the script

## Deployment

This step is necessary only if you want to run it and scan for emails and send out mails

you can make the script execute every once in a while using cronjobs on linux based systems /schedule a task on windows

example to setup cronjob on linux based systems

Run the below command this will open a cron editor
```
crontab -e 
```

Setup the cronjob like

```
* * * * * \path\to\python3 path\to\auto_email.py
```
To read more about cronjobs, please google it