FROM python:3.8-slim-buster
WORKDIR /code

# Upgrade installed packages
RUN apt-get -y update
RUN apt-get -y upgrade

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
