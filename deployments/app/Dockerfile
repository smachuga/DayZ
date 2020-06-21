FROM continuumio/anaconda3
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN python -m compileall
CMD python app.py