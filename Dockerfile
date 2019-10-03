FROM python:3.6-alpine
LABEL maintainer="Craig Derington <cderington@championsg.com>"
RUN apk update && apk upgrade
RUN apk add screen curl
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5580
CMD ["gunicorn", "-b", "0.0.0.0:5580", "-w", "4", "wsgi:app"]
 