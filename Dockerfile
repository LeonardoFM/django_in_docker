FROM python:3.7

RUN apt-get update && apt-get install -y  \
	python3-setuptools \
	python3-pip \
	python3-dev \
	python3-venv \
	git \
	&& \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    mkdir /app

WORKDIR /app


# add current directory code to working directory
ADD . /appp/

# set default environmnet variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# install project dependencies
#RUN pipenv install --skip-lock --system --dev

EXPOSE 8000

CMD python -c "print('hello world')"
