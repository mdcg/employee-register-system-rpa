# employee-register-system-rpa

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mdcg/employee-register-system-rpa/blob/master/LICENSE)

Basically, here is an example of an RPA for employee registration. We are using as a base the system [django-employee-register-system](https://github.com/mdcg/django-employee-register-system).

## Installation

First you will need to download the RPA dependencies. To do this, run the following command:

``` 
> pip install -r requirements.txt
```

Once you have downloaded the dependencies, you will now need a username and password to access the [django-employee-register-system](https://github.com/mdcg/django-employee-register-system). When accessing the [django-employee-register-system](https://github.com/mdcg/django-employee-register-system), there you will have all the information for you to perform this procedure.

Now that you have the username and password, you will need to create a `.env` file that will store them. The process is as follows:

``` 
> cp .env-example .env
```

The above command will copy the contents of `.env-example` to the ` .env` file. Now in the `.env` file we have exactly the structure of the environment variables that RPA will consult to access the [django-employee-register-system](https://github.com/mdcg/django-employee-register-system). Now just add the values ​​corresponding to each of the variables (user and password).

## Generating a list of employees

There is a script here in this project that will generate an extremely useful list with several random employees so that RPA can register. To generate this list, just run the following command:

``` 
> python generate_employee_list.py
```

The generated list will be in CSV format containing 200 employee profiles to be registered by RPA. The generated file already has the name that RPA will try to open by default to consult the data.

## Running

To initialize RPA, you will first need the system of the [django-employee-register-system](https://github.com/mdcg/django-employee-register-system) running on your machine, otherwise the RPA will not work. Once the system we are going to consume is running, you will need to run the following command:

``` 
> python bot.py
```

## Contributing

Feel free to do whatever you want with this project. :-)
