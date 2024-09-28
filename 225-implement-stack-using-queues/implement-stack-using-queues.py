class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # Transfer all elements from q1 to q2
        for x in self.q1:
            self.q2.append(x)

        # Now, q2 contains all elements of q1 in the same order
        # The last element added to q2 is the last element of the stack
        popped_element = self.q2.pop()  # Remove and return the last element
        
        # Clear q1 and transfer all elements back from q2 to q1 except the popped element
        self.q1.clear()
        while self.q2:
            self.q1.append(self.q2.popleft())
        
        return popped_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_element = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return len(self.q1) == 0
