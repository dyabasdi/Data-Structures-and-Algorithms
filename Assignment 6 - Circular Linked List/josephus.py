import sys

class Link():
    """
    Link object
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self):
        """
        double link value
        """
        self.data+=self.data

    def subtract(self):
        """
        zero link value
        """
        self.data-=self.data


class CircularList():
    """
    Circular List of Link objects
    """
    # Constructor
    def __init__ ( self ):
        self.head = None

    # Insert an element (value) in the list
    def insert ( self, data ):
        """
        Inserts new link with value 'data' at end of list
        """
        new_link = Link(data)
        if self.head is None:
            self.head = new_link
            self.head.next=self.head
            return
    # start from beginning
        current_link = self.head
    # go through list until next is Null
        while current_link.next not in (None, self.head):
            current_link = current_link.next
        current_link.next = new_link
        new_link.next = self.head
        return

  # Find the Link with the given data (value)
  # or return None if the data is not there
    def find (self, data):
        """
        Finds Link with value data in list
        """
    # start from the head
        current_link = self.head
        if current_link.data == data:
            return current_link
    # move it forward one so current_link isnt head
        current_link = current_link.next
        for _ in range(self.size()):
            if current_link.data == data:
                return current_link
            current_link = current_link.next
        return None

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
    def delete(self, data):
        """
        Deletes link with value data from list
        """
    # finding data
    # check if list is empty
        val=None
        if self.size()==0:
            return val
        current_link = self.find(data)
    # return None if data not in list
        if current_link is None:
            return val
        if self.head.data==data:
            val=self.head
      #special case for if deleted node is head
            if self.head.next.data == self.head.data:
        #Delete case if only element is head
                self.head.next=None
                self.head=None
            else:
                self.head.data=self.head.next.data
                self.head.next=self.head.next.next
        else:
      #Regular delete with reassignment for pointers
            delete_link=current_link.next
            while delete_link.data != data:
                current_link=current_link.next
                delete_link=current_link.next
            val=delete_link
            current_link.next=delete_link.next
        return val


  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
    def delete_after(self, start, elim_num):
        """
        Deletes nth Link from Link start
        """
        for _ in range(1,elim_num):
      #increment starting link by n-1 steps
            start=start.next
        if start.data==self.head.data:
      #check if deleted node is head
            next_link=self.head.next
        else:
            next_link=start.next
        deleted_link_data=start.data
        self.delete(start.data)
        return deleted_link_data,next_link

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
    def __str__(self):
        """
        Iterates through circular list and appends to normal list then returns as string
        """
        lst=[]
        if self.head is None:
      #checks if list is empty
            return str(lst)
        current_link=self.head
        lst.append(current_link.data)
        current_link=current_link.next
        while current_link.data!=self.head.data:
            lst.append(current_link.data)
            current_link=current_link.next
        return str(lst)

    def size(self):
        """
        returns the number of elements in the circular list
        """
        if self.head is None:
            return 0
        ctr=1
        current_link=self.head
        current_link=current_link.next
        while current_link !=self.head:
            ctr+=1
            current_link = current_link.next
        return ctr

def main():
    """
    Read input and perform Josephus problem
    """
  # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)

  # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

  # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

  # your code
    circle = CircularList()
    for i in range(num_soldiers):
        #create list of soldiers
        circle.insert(i+1)
    current_link=circle.head
    for _ in range(start_count-1):
        #Find very first starting Link
        current_link=current_link.next
    for _ in range(num_soldiers-1):
        #Perform delete operations on list
        del_value, next_link = circle.delete_after(current_link, elim_num)
        #set current_link equal to next_link as that is the link right after the deleted one
        current_link=next_link
        print(del_value)
    if not circle.head is None:
        #check if list is not empty then print last element
        print(circle.head.data)


if __name__ == "__main__":
    main()
