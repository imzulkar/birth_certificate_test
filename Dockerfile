FROM python:3.8.0

COPY ./requirements.txt /rpa/requirements.txt

# Install dependencies
RUN pip3 install -r /rpa/requirements.txt

ENV PYTHONUNBUFFERED 1

# Set the working directory to /rpa
WORKDIR /rpa

# Copy the current directory contents into the container at /rpa
ADD . /rpa/


# executing the main file
CMD ["python", "./main.py"]