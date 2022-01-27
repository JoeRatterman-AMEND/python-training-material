FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install python3 -y

RUN apt install python3-pip -y
RUN python3 -m pip install auto-sklearn
RUN python3 -m pip install pickle-mixin
RUN python3 -m pip install numpy
RUN python3 -m pip install sklearn


COPY . . 
CMD ["python3", "autosklearn_test_script.py"]
