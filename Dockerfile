FROM python:3.8

WORKDIR /usr/src/

RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
RUN apt-get update
RUN apt-get install libmariadb-dev -y
RUN apt-get install libmariadb3 -y

COPY . /usr/src/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r app/requirements.txt

EXPOSE 5000

CMD ["python", "/usr/src/app/main.py"]