FROM python:3.11
WORKDIR /voxus-challenge
COPY . /voxus-challenge
RUN pip install --no-cache-dir -r /voxus-challenge/requirements.txt
CMD ["python", "/voxus-challenge/src/main.py"]