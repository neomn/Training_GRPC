
    docker compose up -d --build
    docker compose run benchmark

-----------------------------------------
Why is gRPC faster?

1- HTTP/2: gRPC uses HTTP/2, which provides several performance benefits:

* Multiplexing: Multiple requests can be sent over a single connection.
* Header Compression: Reduces overhead in subsequent requests.
* Server Push: Server can proactively send resources to the client.


2- Protocol Buffers: gRPC uses Protocol Buffers for serialization, which offers several advantages:

* Binary Format: More compact than text-based formats like JSON.
* Efficient Serialization/Deserialization: Faster to process than parsing JSON.
* Schema-based: Allows for more efficient encoding of data.


3- Code Generation: gRPC generates client and server code, which can be more optimized than general-purpose libraries.
4- Streaming: gRPC's native streaming support can be more efficient for large datasets or real-time updates.

------------------------------------------
How much faster is gRPC?
The performance difference between gRPC and REST can vary significantly depending on the specific use case, 
implementation details, and network conditions. However, here are some general observations:

1- Payload Size: gRPC messages are typically 30% to 40% smaller than equivalent JSON payloads.
2- Serialization/Deserialization: Protocol Buffers can be 6-10 times faster than JSON serialization/deserialization.
3- Overall Performance: In various benchmarks, gRPC has shown to be anywhere from 5 to 20 times faster than REST+JSON, 
especially for larger datasets or high-frequency requests.
4- Latency: Due to HTTP/2 multiplexing, gRPC can significantly reduce latency, especially for multiple parallel requests.


-----------------------------------------
## Rest VS GRPC request lifesycle

### Typical REST Request Lifecycle:

1- Client sends HTTP request
2- Request hits reverse proxy (e.g., Nginx)
3- Proxy forwards to application server (e.g., uWSGI, Gunicorn, PHP-FPM)
4- Application server passes request to web framework (e.g., Django, Flask, Laravel)
5- Web framework middleware processes request
6- Route matching occurs
7- Controller/view function is called
8- Response is generated and passes back through the layers
9- Client receives HTTP response

### gRPC Request Lifecycle:

1- Client makes gRPC call
2- gRPC client library handles serialization
3- Request goes directly to gRPC server
4- gRPC server handles deserialization
5- Service method is called directly
6- Response is serialized and sent back
7- Client receives and deserializes response


## interceptors in grpc ( used for authentication )
