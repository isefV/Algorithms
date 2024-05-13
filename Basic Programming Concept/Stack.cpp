#include<iostream>

template <class T>
class Stack{
    private:
        Stack* top;
        Stack* prev;
        T data;
        int count;

    public:
        Stack();
        void push(T);
        T get_top();
        T pop();
        void DisplayStack();
        bool del_stack();
        int get_count();
};

template <class T> Stack<T>::Stack(){
    top=nullptr;
    prev=nullptr;
    count=0;
}

template <class T>void Stack<T>::push(T tempData){
    Stack* node = new Stack();
    node->data=tempData;
    if(count==0){
        node->prev=nullptr;
    }
    else{
        node->prev=top;
    }
    top=node;
    count++;
}

template <class T>T Stack<T>::get_top(){
    T nodeData = top->data;
    return nodeData;
}

template <class T>T Stack<T>::pop(){
    Stack* tempNode=top;
    T nodeData = tempNode->data;
    top=tempNode->prev;
    delete tempNode;
    count--;
    return nodeData;
}

template <class T>void Stack<T>::DisplayStack(){
    Stack* tempNode=top;
    std::cout<<"Top of Stack is :"<<tempNode->data<<"\nStack items :\t";
    for(int i=0;i<count;i++){
        std::cout<<tempNode->data<<"\t";
        tempNode=tempNode->prev;
    }
}

template <class T>bool Stack<T>::del_stack(){
    int cnt=count;
    for(int i=0;i<cnt;i++){
        Stack* tempTop=top;
        top=tempTop->prev;
        delete tempTop;
        count--;
        if(count == 0) return true;
    }
    return false;
}
template <class T>int Stack<T>::get_count(){
    return count;
}

int main()
{
    Stack<char> P1;
    P1.push('n');
    P1.push('5');
    P1.push('b');
    char t=P1.get_top();
    int c=P1.get_count();
    std::cout<<"Top item :"<<t<<"\tCount is :"<<c<<"\n";
    P1.push('4');
    P1.push('a');
    P1.DisplayStack();
    char a=P1.pop();
    c=P1.get_count();
    std::cout<<"\tCount is :"<<c<<"\n";
    char b=P1.pop();
    std::cout<<"Poped item :"<<a<<"\t"<<b<<"\n";
    std::cout<<P1.del_stack()<<"\n";
    P1.DisplayStack();

    return 0;
}