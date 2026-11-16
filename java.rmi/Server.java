// https://docs.oracle.com/javase/7/docs/technotes/guides/rmi/hello/hello-world.html

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server implements Hello {
    public String sayHello() {
        return "Hello, world!";
    }

    public static void main(String args[]) {
        try {
            Server obj = new Server();
            Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 5002);

            Registry registry;
            try {
                registry = LocateRegistry.createRegistry(1099);
            } catch (java.rmi.server.ExportException e) {
                registry = LocateRegistry.getRegistry(1099);
            }
            registry.rebind("Hello", stub);

            System.out.println("Server ready");

        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
