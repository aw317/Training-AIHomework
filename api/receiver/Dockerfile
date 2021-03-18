FROM python:3.7-alpine
WORKDIR /receiver
ENV FLASK_APP=app.py:create_receiver_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["flask", "run"]
