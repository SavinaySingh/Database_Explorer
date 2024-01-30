# Database Explorer Web App

## Description
<What your application does>
The application is a database explorer that first extablishes a connection to a postgres database and then stores the table in the form of pandas dataframe. Then it displays the output analysis in five tabs: Overall, Numeric, Explore, Text and Date. 

    <img width="603" alt="image" src="https://github.com/SavinaySingh/Database_Explorer/assets/21008903/c899c9ac-de1c-4879-b2cf-9e4326bdbb93">


<Some of the challenges you faced>
<pre>
Challenges:
1.	As the config file was not completed on time, I had to populate the session state for db, table_selected and schema_selected.
2.	As the session state was not populated using config file, there was an issue of nested streamlit expander which occurred as the instance of PostgresConnector was called multiple times. So, to solve this, I commented out the streamlit expander function in open_connection() of database/logics.py.
3.	While running the docker compose file on my mac machine, I was getting an error ‘SCRAM authentication requires libpq version 10’ . This appears to be an issue in libpg upstream that is causing it to build against the incorrect library version on ARM in mac M1 machines. This was solved by running it via rosetta by following command: export DOCKER_DEFAULT_PLATFORM=linux/amd64
</pre>

<Some of the features you hope to implement in the future>
<pre>
Future work:
1.	The project structure in the default template needs to be updated as src folder, dockerfile and requirements file are placed outside the app folder. This creates an issue while writing the docker-compose yaml file.
2.	Serie_date, Serie_Numeric and Serie_text can all be merged into one module as they all have similar functionalities.
3.	The application's front end and back end may be independent, which would make the application's programming simpler.
</pre>
    
## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
<pre>
1. To launch the application the initial step is to change the directory to the project directory: cd /project_dsp
2. Multi-container Docker applications can be defined and run using the Docker Compose. The micro-services of the application can be configured using Compose using a YAML file. The following commands should be entered in the terminal to construct and launch the docker container in the second step: 
    docker-compose build
    docker-compose up
3. The following command can be used to terminate the docker containers:
    docker-compose down
</pre>
<Which Python version you used>
<Which packages and version you used>
<pre>
Requirements
python==3.8.2
psycopg2-binary==2.9.5
pandas==1.5.1
streamlit==1.13.0
</pre>


## Project Structure
<List all folders and files of this project and provide quick description for each of them>
<pre>
DSP_AT3_16-main/
    .DS_Store
    README.md
    docker-compose.yml
    app/
        .DS_Store
        requirements.txt
        Dockerfile
        streamlit_app.py
        src/
            .DS_Store
            config.py
            __init__.py
            database/
                __init__.py
                display.py
                logics.py
                queries.py
                __pycache__/
                    logics.cpython-38.pyc
                    __init__.cpython-38.pyc
                    queries.cpython-38.pyc
            dataframe/
                __init__.py
                display.py
                logics.py
                queries.py
            serie_text/
                __init__.py
                display.py
                logics.py
                queries.py
            test/
                test_database_logics.py
                __init__.py
                test_serie_date_queries.py
                test_dataframe_logics.py
                test_dataframe_queries.py
                test_serie_text_logics.py
                test_serie_numeric_queries.py
                test_database_queries.py
                test_serie_date_logics.py
                test_serie_text_queries.py
                test_serie_numeric_logics.py
            __pycache__/
                __init__.cpython-38.pyc
            serie_numeric/
                __init__.py
                display.py
                logics.py
                queries.py
                __pycache__/
                    logics.cpython-38.pyc
                    __init__.cpython-38.pyc
                    display.cpython-38.pyc
                    queries.cpython-38.pyc
            serie_date/
                __init__.py
                display.py
                logics.py
                queries.py
</pre>
    
## Citations
    
<Mention authors and provide links code you source externally>
<pre>
1. PSYCOPG2. PyPI. (2022, October 25). Retrieved from https://pypi.org/project/psycopg2/ 
2. Vega-Altair: Declarative visualization in python. Altair. (n.d.). Retrieved from https://altair-viz.github.io/ 
</pre>

## Author
Name: Savinay Singh\
Student ID: 24591935\
Name: Prinston Mascarenhas\
Student ID: 24587331\
Name: Sagar Sudhir Bhagwatkar\
Student ID: 24613616\
Name: Steffi Grace Tensingh\
Student ID: 24592774
