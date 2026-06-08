class node:

    def __init__(self,data):
        self.data=data
        self.next=None
        #creates a node, the "self.data=data" stores the values
        #the self.next=None implies that the node isnt pointing to any other node
def traversal(head):
    current=head                    #assigning variable to the head
    while current:                  #loop to traverse 
        print(current.data)         #prints the current value the vairable represents
        current=current.next        #manually moves the variable to the next node
def insert_at_begining(head,data):
    newnode=node(data) #creating a new node
    newnode.next=head  #it makes the new node point to the current head
    return newnode     #newnode becomes head
    #Key idea:
    #New node points to old head
    #New node becomes head
def Insert_at_end(head,data):
    newnode=node(data)  #1st step is always create a new node
    
    if not head:        #👉 If the list is empty (head = None):
        return newnode  #There is no list yet
                        #So this new node becomes the first node
    current=head
    while current.next:
        current=current.next    #you start at the head and keep moving further and stop when current.next==none

    current.next=newnode        #attaching new node
    return head                 #head doesnt change, thats why return the same head
 #Traverse to last node
 #Attach new node
def Insert_at_position(head,data,pos):
    newnode=node(data)
    if pos==0:
        newnode.next=head
        return newnode
    
    current=head
    for i in range(pos-1):
        current=current.next

    newnode.next=current.next
    current.next=newnode

    return head

    '''Step-by-step:
    Create a new node with the given data
    If pos == 0:
    Insert at the beginning
    Point new node to current head
    Return new node as new head
    Otherwise:
    Traverse the list until the node just before the target position (pos - 1)
    Adjust pointers:
    new_node.next = current.next
    current.next = new_node
    Return the original head (since head doesnt change here)'''


    



a=node(10)
b=node(20)
c=node(30)
d=node(40)

a.next=b
b.next=c
c.next=d
traversal(a)
insert_at_begining(a,15)
Insert_at_end(a,45)
traversal(a)




    
        