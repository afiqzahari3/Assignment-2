import java.net.*;
import java.io.*;

public class client
{
	public static void main(String[] args)
	{
		String host = "192.168.233.128";
		int port = 19999;
		StringBuffer instr = new StringBuffer();
		String TimeStamp;
		System.out.println("SocketClient Initialized");
		
		while(1){
		try
		{
			InetAddress address = InetAddress.getByName(host);
			Socket connection = new Socket(address, port);
			BufferedOutputStream bos = new BufferedOutputStream(connection.getOutputStream());
		       OutputStreamWriter osw = new OutputStreamWriter(bos, "US-ASCII");
	       TimeStamp = new java.util.Date().toString();
		String process = "Calling the socket server on " + host + " port"+ port+" at "+ TimeStamp + (char)13;
 		
		osw.write(process);
		osw.flush();

		BufferedInputStream bis = new BufferedInputStream(connection.getInputStream());
		InputStreamReader isr = new InputStreamReader (bis, "US-ASCII");		int c;
		while ((c= isr.read())!=13)
			instr.append((char)c);
		
		connection.close();
		System.out.println(instr);
}}

catch (IOException f)
{
	System.out.println("IOException; "+ f);
}
catch (Exception g)
{
	System.out.println("Exception "+ g);
}
}
}
