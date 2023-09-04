# grpc-python

## Step 1: Install `pip`
```zsh
sudo apt install python3-pip
```

## Step 2: Install `grpc-tools`
```zsh
pip3 install grpcio-tools
```
If not install then you have to upgrade pip3
```zsh
pip3 install --upgrade pip
```

##  Step 3: Create a proto file
on path `demo1-grpc-python/protos/greet.proto` write `proto` code

This file is generally generated while making the gRPC projects
<details>
<summary>Example</summary>

```python
syntax = "proto3";

package greet;

// The greeting service definition.
service Greeter {
	// Unary
	rpc SayHello (HelloRequest) returns (HelloReply);

	// Server Streaming
	rpc ParrotSaysHello (HelloRequest) returns (stream HelloReply);
	
	// Client Streaming
	rpc ChattyClientSaysHello (stream HelloRequest) returns (DelayedReply);

	// Both Streaming
	rpc InteractingHello (stream HelloRequest) returns (stream HelloReply);
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
  string greeting = 2;
}

// The response message containing the greetings.
message HelloReply {
  string message = 1;
}

message DelayedReply {
	string message = 1;
	repeated HelloRequest request = 2;
}
```

</details>

## Step 4: generate the bolierplate code needed for creating client and server

```zsh
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto
```

## step 5: To run the program use two terminal one for server and another for client

To run server
```zsh
python3 greet_server.py
```

To run client
```zsh
python3 greet_client.py
```

