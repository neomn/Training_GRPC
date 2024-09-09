
    python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/service.proto
    docker compose up --build
    python grpc_client.py
    python rest_client.py
    python benchmark.py
