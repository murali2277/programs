import java.util.*;
class Node{
    int data;
    Node next;
    public Node(int data){
        this.data=data;
        next=null;
    }
}
class LinkedList{
    Node head;
    void insert(int data){
        Node nw=new Node(data);
        if(head==null){
            head=nw;
            return;
        }
        Node temp=head;
        while(temp.next!=null){
            temp=temp.next;
        }
        temp.next=nw;
    }
    void display(){
        Node temp=head;
        while(temp!=null){
            System.out.println(temp.data);
            temp=temp.next;
            if(temp!=null){
                System.out.println("");
            }
        }
    }
}
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        LinkedList ll=new LinkedList();
        int size=sc.nextInt();
        int num;
        for(int i=0;i<size;i++){
            num=sc.nextInt();
            ll.insert(num);
        }
        ll.display();
    }
}