FROM python:3.10.0

WORKDIR /root/Clone

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U pip && pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Clone"]
