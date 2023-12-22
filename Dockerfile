FROM python:3.11
WORKDIR /voxus-challenge
COPY . /voxus-challenge
RUN pip install --no-cache-dir -r /challenge/requirements.txt
CMD ["python", "/challenge/src/main.py"]
