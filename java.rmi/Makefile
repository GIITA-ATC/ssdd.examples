.PHONY: all run-registry run-server run-client clean

SERVER_HOST ?= 192.168.1.34

all: Server.class Client.class Hello.class

%.class: %.java
	javac $<

run-registry:
	rmiregistry

run-server:
	java -classpath . -Djava.rmi.server.hostname=$(SERVER_HOST) Server

run-client:
	java -classpath . Client $(SERVER_HOST)

clean:
	$(RM) *.class *~
