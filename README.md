## FlaskQL
A Python, Graphene and SQL Alchemy Project

``` https://docs.graphene-python.org ```

#### Project Outline
* Installation
* Installing dependencies
* Creating our schema
* Define the data models
* Add some test data
* Test our Graph


#### Installation

First, create a new virtual envionment for our Graphene project and install the dependent libraries.

```
$ virtualenv .env --python=python3
$ source .env/bin/activate
```
Next, install the project dependencies

```
(.env)$ pip3 install -r requirements-dev.txt
```

#### Define Data Model
This project demonstrates the integration of Python, SQLite3, SQL Alchemy, and Graphene.  This project contains 5 data models:

```
DataCenter
Router
Switch
Computer
Process
```

#### Create the Schema & Node Relay Connections

```
DataCenterConnection
RouterConnection
SwitchConnection
ComputerConnection
ProcessConnection
```

#### Run the FlaskQL App

```
(.env)$ python ./app.py
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5580/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 623-353-961
```

#### Browse to the Graph endpoint

Point your web browser to http://0.0.0.0:5580/graphql

#### Example Queries

```
{ allDatacenters {
    edges {
        node {
            id
            name
            accessNetwork
            streetAddress
            city
            state
            fabric
            }
        }
    } 
}

{ allRouters {
    edges {
        node {
            id
            name
                datacenter {
                    id
                    name
                    fabric
                }
            }
        }
    } 
}

```
