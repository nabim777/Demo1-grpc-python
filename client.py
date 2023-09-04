import grpc
import greet_pb2
import greet_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = greet_pb2_grpc.GreetingServiceStub(channel)
    
    name = input("Enter your name: ")
    request = greet_pb2.HelloRequest(name=name)
    
    response = stub.SayHello(request)
    print(response.greeting)

if __name__ == '__main__':
    run_client()
