# pythonDemo
python code demo

1、下载安装protobuf  
git clone https://github.com/google/protobuf.git  
2、生成protobuf的Python类  
./protoc --python_out=OUT_DIR -I=IN_DIR person.proto  
./protoc protobuf程序  
--python_out 文件输出地址  
-I 转换文件所在地址  
person.proto 要转换的文件  
3、demo.py protobuf 序列化、反序列化例子   
serSock.py、cliSock.py 用socket传输protobuf的例子  
person.proto proto文件  
person_pb2.py proto文件转换生成的Python类  
