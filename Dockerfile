FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

EXPOSE 8888

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
