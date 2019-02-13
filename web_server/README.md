# project-vending-machine: Web Server

This directory contains a [Django](https://www.djangoproject.com/) app, written in python, that controls the database, web app, and other key parts for our vending machine.

## Getting Started

### Quick Demo

`Remix with Glitch` & `Deploy with Heroku` buttons coming soon!

### Prerequisites

Make sure you have the following installed:

- [`python3`](https://www.python.org/downloads/)
- [`pip`](https://pip.pypa.io/en/stable/installing/)
- [`pipenv`](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) - install with `pip install pipenv --user`

### Installing

Make sure you have the `project-vending-machine` repo cloned already, then:

``` bash
cd web_server
pipenv install
pipenv shell
python manage.py runserver
```

And your server is running!

When you do `python manage.py runserver`, you might see warning message like:

```
python manage.py runserver
You have 15 unapplied migration(s). Your project may not work properly until you...
```

This has to do with how Django takes care of databases - which means you'll occasionally need to "migrate" database changes, like so:

```bash
python manage.py migrate
```

Now, head to http://localhost:8000 to see your webserver running!

### Configuration

This Django app uses a `.env` file to safely store secrets like passwords or API keys - so that way you don't accidentally commit your secrets to GitHub!

To configure your secrets, copy and paste the [`.env.sample`](https://github.com/asg017/project-vending-machine/blob/master/.env.sample) file into a file called `.env`, and add your secrets ONLY to that new `.env` file.

Here are all the key/values that should be in your .env file:

|Key|Description|Example
|-|-|-
|`DJANGO_SECURITY_KEY`|A secure password that Django uses for encryption/security|`DJANGO_SECURITY_KEY=QxcT0L%11E*!pbKScP$nRz`
|`GITHUB_PERSONAL_ACCESS_TOKEN`|A secret token generator by GitHub used to automatically comment on new issues/PR's - generate [here](https://github.com/settings/tokens) |`GITHUB_PERSONAL_ACCESS_TOKEN=abc978de86bcd8e7850`
|`GITHUB_WEBHOOK_SECRET`|A secure password to verify that an incoming GitHub webook message is indeed from GitHub|`GITHUB_WEBHOOK_SECRET=r!S@!PEr2UM@z$Bomi2@XQd`

#### DJANGO_SECURITY_KEY error

If you tried running `python manage.py runserver` but got a warning about including a secret in a `.env` file, make sure you have a `.env` file in the parent directory. There should be a `.env.sample` file in that folder, you can copy/paste or run `cp .env.sample .env` to make your own. Make sure to replace those values with actual secure passwords! ([password generator](https://1password.com/password-generator/))



