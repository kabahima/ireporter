## About

iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Features

- Users can create an account and log in

- Users can create a red-flag record (An incident linked to corruption

- Users can create intervention record (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c)

- Users can edit their red-flag or intervention records

- Users can delete their red-flag or intervention records

- Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records

- Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records

- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved)

- Users can add images to their red-flag or intervention records, to support their claims

- Users can add videos to their red-flag or intervention records, to support their claims

## Getting Started

Clone the project from this [link](https://github.com/kabahima/ireporter.git)

## Prerequisites

* A computer with an operating system (Linux, MacOS or Windows can do the job)
  Python 3.6
* Pytest or any other preffered python tesing tool
* Postman to test the API endpoints
* A preffered text editor
* Git to keep track of the different project branches

## Installing

Clone the project from this [link](https://github.com/kabahima/ireporter.git)

Open your terminal or command prompt for windows users

Type

```
$ cd ireporter
$ virtualenv venv
$ pip install -r requirements.txt
$ python run.py
```

## Deployment

The API is hosted on Heroku. Use the link below to navigate to it.

[heroku](https://git.heroku.com/ireporter56.git)

## Testing the Api

Run the command below to install pytest in your virtual environment

`$ pip install pytest`

Run the tests

`$ pytest -v`

## Endpoints

| Endpoint          | Functionality |
| --------          |     --------- |
| `GET /api/v1/red-flags` | Fetch all redflag records |
| `GET /api/v1/interventions` | Fetch all intervention records |
| `GET /api/v1/red-flags/<incident_id>` | Fetch a specific redflag record |
| `GET /api/v1/interventions/<incident_id>` | Fetch a specific intervention record |
| `DELETE /api/v1/red-flags/<incident_id>` | Delete a specific redflag record |
| `DELETE /api/v1/interventions/<incident_id>` | Delete a specific intervention record |
| `PATCH /api/v1/red-flags/<incident_id>/location` | Edit redflag record's location |
| `PATCH /api/v1/intervention/<incident_id>/location` | Edit intervention record's location |
| `PATCH /api/v1/red-flags/<incident_id>/comment` | Edit redflag record's comment |
| `PATCH /api/v1/interventions/<incident_id>/comment` | Edit intervention record's comment |
| `PATCH /api/v1/red-flags/<incident_id>/status` | Change redflag record's status |
| `PATCH /api/v1/interventions/<incident_id>/status` | Change intervention record's status |
| `POST /api/v1/red-flags` | Create a redflag record |
| `POST /api/v1/interventions` | Create an intervention record |
| `POST /api/v1/users` | Create user account |
| `POST /api/v1/users/login` | Login user or admin |

## Built With

 Python 3.6.5
 Flask (A python microframework)

## Tools Used

* Pylint
* Pytest
* Virtual environment
