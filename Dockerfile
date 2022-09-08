# Pull base image
FROM python:3.7.9
# Set environment varibles
WORKDIR /code/
# Install dependencies
RUN apt-get update
COPY . /code/
RUN apt-get install python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
