import java.util.Stack;

public class LinkedListUsingStack {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    private String emptyLinkedListErrorMessage = "LinkedList is empty"; 

    public LinkedListUsingStack(){
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void add(int value){
        stack1.push(value);
    }

    public int remove(){
        if(stack1.isEmpty()){
            throw new RuntimeException(emptyLinkedListErrorMessage);
        }
        while(!stack1.empty()){
            stack2.push(stack1.pop());
        }
        
        int popped = stack2.pop();
        
        while(!stack2.empty()){
            stack1.push(stack2.pop());
        }

        return popped;
    }

    public int peek(){
        if(stack1.empty()){
            throw new RuntimeException(emptyLinkedListErrorMessage);
        }
        while(!stack1.empty()){
            stack2.push(stack1.pop());
        }
        int first = stack2.peek();
        while(!stack2.empty()){
            stack1.push(stack2.pop());
        }
        return first;
    }

    public boolean isEmpty(){
        return stack1.isEmpty();
    }

    public int size(){
        return stack1.size();
    }

    public void print(){
        if(stack1.isEmpty()){
            throw new RuntimeException(emptyLinkedListErrorMessage);
        }
        while(!stack1.empty()){
            stack2.push(stack1.pop());
        }
        System.out.print("HEAD -> ");
        while(!stack2.isEmpty()){
            int temp = stack2.pop();
            System.out.print(temp+" -> ");
            stack1.push(temp);
        }
        System.out.println("NULL");
    }


    public static void main(String[] args){
        LinkedListUsingStack list = new LinkedListUsingStack();

        list.add(10);
        list.add(20);
        list.add(30);

        System.out.println("Elements in LinkedList: ");
        list.print(); // Output: 10 20 30

        System.out.println("Front element: " + list.peek()); // Output: 10

        System.out.println("Removed element: " + list.remove()); // Output: 10

        System.out.println("Elements in LinkedList after removal: ");
        list.print(); // Output: 20 30
    }
}
