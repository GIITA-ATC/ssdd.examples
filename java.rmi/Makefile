.PHONY: all run-registry run-server run-client clean

all: Server.class Client.class Hello.class

%.class: %.java
	javac $<

run-registry:
	rmiregistry

run-server:
	java -classpath . -Djava.rmi.server.codebase=file:./ Server 9000

run-client:
	java -classpath . Client localhost 9000

clean:
	$(RM) *.class *~
