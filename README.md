# STREAMLIT APPLICATION!

## Author
Name: Savinay Singh\
Student ID: 24591935

## Description
<What your application does>
<Some of the challenges you faced>
<Some of the features you hope to implement in the future>

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
<Which Python version you used>
<Which packages and version you used>
<pre>
python==3.8.2
psycopg2-binary==2.9.5
pandas==1.5.1
streamlit==1.13.0
</pre>

## How to Run the Program
<Provide instructions and examples>
To start the docker containers:\
    >docker-compose build\
    >docker-compose up\
To stop the docker containers:\
    >docker-compose down


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
        test.py
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
