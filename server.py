import grpc
from concurrent import futures  # Import ThreadPoolExecutor from concurrent module
import greet_pb2
import greet_pb2_grpc

class GreetingServicer(greet_pb2_grpc.GreetingServiceServicer):
    def SayHello(self, request, context):
        response = greet_pb2.HelloResponse()
        response.greeting = f"Hello, {request.name}!"
        return response

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Use futures.ThreadPoolExecutor
    greet_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
