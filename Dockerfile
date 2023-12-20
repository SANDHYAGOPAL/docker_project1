# FROM python:3-alpine3.15
# WORKDIR /app
# COPY . /app

# RUN pip install -r requirement.txt
# EXPOSE 5000
# CMD python ./app.py

FROM python:3-alpine3.15
WORKDIR /app 
COPY . /app
# COPY . /templates
# COPY . /req
# RUN pip install -r req/requirements.txt
RUN pip install flask
CMD ["python", "app.py"]  