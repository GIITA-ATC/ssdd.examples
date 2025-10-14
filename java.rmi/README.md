# Java RMI Example
This example demonstrates a simple Java RMI server and client.

Following steps can be followed to set up and run the example. A Makefile is also provided with necessary commands.

### 1. Install dependencies
Install the required JDK package:

```bash
sudo apt install openjdk-21-jdk-headless
```

### 2. Change Java version (if needed)
If you have multiple Java versions installed, select the desired one:

```bash
sudo update-alternatives --config java
```

### 3. Compile
Compile all Java source files:

```bash
javac *.java
```

### 4. Run the RMI registry
Start the RMI registry in the background:

```bash
rmiregistry &
```

### 5. Run the server
Start the RMI server:

```bash
java -classpath . -Djava.rmi.server.codebase=file:./ Server 9000
```

### 6. Run the client (in another terminal)
Start the RMI client:

```bash
java -classpath . Client localhost 9000
```
