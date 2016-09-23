# redshift-csv-inserter
Super quick and dirty way to insert local CSV files into Redshift. Assumes you're running Python 2.x. It'll try to insert everything as a string so you'll have to modify it to handle numeric types.

## Requirements

Install requirements with:

```
pip install -r requirements.txt
```

## Installation

None. Clone this repo and go.

## Setup

There is a configuration file `config.yaml.template` with the following:

```
# Redshift
redshift_endpoint: '<name>.<id>.<region>.redshift.amazonaws.com'
redshift_user: 'admin'
redshift_password: 'password'
redshift_port: '5439'
redshift_database: 'dev'
table_name: 'test_table'
columns: 'column1, column2, column3, column4'
```

Modify these to the correct parameters listed in the AWS console then change the name of the file to config.yaml.


## Usage

Give as an argument to the script the CSV file you want to load to Redshift.

```
python redshift_csv_inserter.py file.csv
```
