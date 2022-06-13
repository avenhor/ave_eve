FROM python:3-slim
ADD . /python-flask
WORKDIR /python-flask
RUN apt update && apt upgrade -y && apt install apache2-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./eve.py", "host=0.0.0.0"]