FROM python:3.11.4

WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/anayaml/voxus-challenge.git /voxus-challenge
WORKDIR /voxus-challenge
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
