import time

import make87
import torch
from make87_messages.tensor.matrix_44_pb2 import Matrix44
from make87_messages.core.header_pb2 import Header


def main():
    make87.initialize()
    topic = make87.get_publisher(name="OUTPUT_MATRIX", message_type=Matrix44)

    print("CUDA available:", torch.cuda.is_available())

    while True:
        torch_matrix = torch.rand(4, 4)
        message = Matrix44(header=make87.create_header(Header, entity_path="/"))

        (message.m00, message.m01, message.m02, message.m03) = torch_matrix[0]
        (message.m10, message.m11, message.m12, message.m13) = torch_matrix[1]
        (message.m20, message.m21, message.m22, message.m23) = torch_matrix[2]
        (message.m30, message.m31, message.m32, message.m33) = torch_matrix[3]

        topic.publish(message)
        print(f"Published: {message}")
        time.sleep(1)


if __name__ == "__main__":
    main()
