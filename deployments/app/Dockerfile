FROM python:3-alpine
ADD app/ /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m compileall
CMD python app.py