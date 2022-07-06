//C++ Program to implement Linked List-Tail

#include<iostream.h>

using namespace std;

class Node
{
    public:
    int data;
    Node *nex;
};

class LinkedList
{
    private:
        Node* head;
    public:
        LinkedList() { 
        head = NULL;
    }
        int calcSize();
        void insert_Last(int data);
        void display();
};

void LinkedList::insert_Last(int data){

    Node* freshNode = new Node();

    freshNode->data = data;
    
    freshNode->nex = NULL;

    
    if(head==NULL){
        head = freshNode;
        cout << freshNode->data << " inserted" << endl; 
        return; 
    } 
    struct Node* temp = head; 
    
    while(temp->nex!=NULL)
        temp = temp->nex;

    
    temp->nex = freshNode;
    cout << freshNode->data << " inserted" << endl;
}

void LinkedList::display(){
    
    Node* node = new Node();
    node = head;
    
    
    while(node!=NULL){
        cout << node->data << " "; 
        node = node->nex;
    }
    cout << endl; 
} 

int main() 
{ 
    LinkedList* my_list = new LinkedList(); 
    my_list->insert_Last(7);
    my_list->insert_Last(8);
    my_list->insert_Last(9);
    my_list->insert_Last(10);


    my_list->display(); 
    return 0;  
}



