import time
import grpc
import service_pb2
import service_pb2_grpc
import requests

def benchmark_grpc(num_requests):
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = service_pb2_grpc.GreeterStub(channel)
    
    start_time = time.time()
    for _ in range(num_requests):
        stub.SayHello(service_pb2.HelloRequest(name='World'))
    end_time = time.time()
    
    return end_time - start_time

def benchmark_rest(num_requests):
    start_time = time.time()
    for _ in range(num_requests):
        requests.post('http://rest_server:5000/hello', json={"name": "World"})
    end_time = time.time()
    
    return end_time - start_time

if __name__ == '__main__':
    num_requests = 1000
    
    # Wait for servers to be ready
    time.sleep(5)
    
    grpc_time = benchmark_grpc(num_requests)
    rest_time = benchmark_rest(num_requests)
    
    print(f"gRPC time for {num_requests} requests: {grpc_time:.2f} seconds")
    print(f"REST time for {num_requests} requests: {rest_time:.2f} seconds")
    print(f"gRPC is {rest_time / grpc_time:.2f}x faster than REST")
