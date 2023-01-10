FROM python:3.11-slim-buster

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    git \
    python3 \
    python3-dev \
    build-essential

WORKDIR /app

COPY . /app 
RUN python setup.py bdist_wheel
RUN pip3 install dist/*.whl

COPY . /app 
# RUN pip3 install wheels/*.whl

ENTRYPOINT [ "/bin/sh" ]
CMD ["./run.sh"]