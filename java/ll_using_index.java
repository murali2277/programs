import java.util.*;
import java.io.*;

class Node {
	int data;
	Node next;

	Node(int d)
	{
		data = d;
		next = null;
	}
}

public class LinkedList {

	static Node head,tail; //by default initialized to null

	public static void add(int data)
	{
	    Node temp = new Node(data);
	    temp.next = null;
	    
	    if(head == null)
	       head = tail = temp;
	   else
	   {
	        tail.next = temp;
	        tail = temp;
	   }
	}
	
	public static void insert(int value,int position)
	{
     //add code here

	}

	// Method to print the LinkedList.
	public static void display()
	{
		Node currNode = head;
	
		while (currNode != null) {
			System.out.print(currNode.data + " ");
			currNode = currNode.next;
		}
		System.out.println();
	}
	
	public static void main(String[] args)
	{
	    Scanner sc = new Scanner(System.in);
	    int val;
		LinkedList list = new LinkedList();
		// add 4 nodes
		add(10);
		add(20);
		add(30);
		add(40);
		//insert at position
		int pos = sc.nextInt(); //position to insert
		val = sc.nextInt(); //value to insert
		insert(val,pos);
		
		// call this function only for valid positions...add logic for the same
		display();
	}
}
