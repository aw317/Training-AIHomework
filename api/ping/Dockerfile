FROM python:3.7-alpine
WORKDIR /ping
ENV FLASK_APP=app.py:create_ping_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
RUN apk add --no-cache gcc musl-dev linux-headers curl
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
HEALTHCHECK --interval=5s --timeout=3s CMD curl --fail http://localhost:8080/health || exit 1
CMD ["flask", "run"]
