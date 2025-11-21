import java.io.*;
import java.net.*;
class usr
{
public static void main(String args[]) throws Exception
{
DatagramSocket serverSocket = new DatagramSocket(9876);
byte[] receivebuffer = new byte[1024];
byte[] sendbuffer = new byte[1024];
while(true)
{
DatagramPacket recvdpkt = new DatagramPacket(receivebuffer, receivebuffer.length);
serverSocket.receive(recvdpkt);
InetAddress IP = recvdpkt.getAddress();
int portno = recvdpkt.getPort();
String clientdata = new String(recvdpkt.getData());
System.out.println("\nClient : "+ clientdata);
System.out.print("\nServer : ");
BufferedReader serverRead = new BufferedReader(new InputStreamReader (System.in) );
String serverdata = serverRead.readLine();
sendbuffer = serverdata.getBytes();
DatagramPacket sendPacket = new DatagramPacket(sendbuffer, sendbuffer.length, IP,portno);
serverSocket.send(sendPacket);
}
}
}