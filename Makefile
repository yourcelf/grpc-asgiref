.PHONY: proto clean test

proto:
	python -m grpc_tools.protoc \
		--proto_path="." \
		--python_out="." \
		--grpc_python_out="." \
		threadname.proto

clean:
	rm threadname_pb2.py threadname_pb2_grpc.py

requirements.txt:
	poetry export -f requirements.txt --dev --output requirements.txt
