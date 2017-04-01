

default: server

server.o: server.c 
    gcc -c server.c -o server.o

server: server.o
    gcc server.o -o server

clean:
    -rm -f server.o
    -rm -f server