FROM python:3.12-bullseye

WORKDIR /app
COPY dependencias.txt .
RUN pip install -r dependencias.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "lms.asgi:application", "--host", "0.0.0.0", "--port", "8080", "--reload"]