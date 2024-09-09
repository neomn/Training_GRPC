FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/service.proto

CMD ["python", "grpc_server.py"]
