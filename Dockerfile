FROM python:3.11
WORKDIR /challenge
COPY . /challenge
RUN pip install --no-cache-dir -r /challenge/requirements.txt
CMD ["python", "/challenge/src/main.py"]
