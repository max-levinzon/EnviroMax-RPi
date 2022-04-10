FROM python:3.9.8

RUN apt-get update && apt-get install -y \
gcc build-essential

RUN python -m pip install --upgrade pip

RUN mkdir EnviroMax
ADD . EnviroMax/
WORKDIR /EnviroMax/

RUN python3 -m venv enviroEnv
RUN enviroEnv/bin/pip install -r requirements.txt

RUN cat main.py