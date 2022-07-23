FROM python:3-alpine
RUN apk add --no-cache tzdata

RUN mkdir -p /data

WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py sync.py bringapi.py grocylist.py ./

CMD ["python", "./main.py"]
VOLUME ["/data"]
