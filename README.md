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

## Step 3: generate the bolierplate code needed for creating client and server

No need to do this step since already `greet_pb2.py` and `greet_pb2_grpc.py` already generated

```zsh
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto
```

## step 4: To run the program use two terminal one for server and another for client

To run server
```zsh
python3 greet_server.py
```

To run client
```zsh
python3 greet_client.py
```

## For presentation link [click here](https://www.canva.com/design/DAFqZ4YPy98/79UULeTKa-O1KvA7-2ZuUA/edit)