import java.io.*;
import java.net.*;
class ucl
{
public static void main(String args[]) throws Exception
{
BufferedReader clientRead =new BufferedReader(new InputStreamReader(System.in));
DatagramSocket clientSocket = new DatagramSocket();
InetAddress IP = InetAddress.getByName("127.0.0.1");
byte[] sendbuffer = new byte[1024];
byte[] receivebuffer = new byte[1024];
System.out.print("\nClient: ");
String clientData = clientRead.readLine();
sendbuffer = clientData.getBytes();
DatagramPacket sendPacket =
new DatagramPacket(sendbuffer, sendbuffer.length, IP, 9876);
clientSocket.send(sendPacket);
DatagramPacket receivePacket =
new DatagramPacket(receivebuffer, receivebuffer.length);
clientSocket.receive(receivePacket);
String serverData = new String(receivePacket.getData());
System.out.print("\nServer: " + serverData);
clientSocket.close();
}
}