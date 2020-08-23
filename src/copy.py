from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
import os
import sys

mc = Minio(os.environ['MINIO_SERVICE_HOST']+ ':' + os.environ['MINIO_SERVICE_PORT'],
                    access_key='minio',
                    secret_key='minio_password',
                    secure=False)

if __name__ == '__main__':
    print(sys.argv)
    # mc.fput_object('mat', 'result.txt', '/workspace/filedrop/result.txt')
    print(mc.fput_object('mat', sys.argv[1], sys.argv[2]))