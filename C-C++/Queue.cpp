#include <iostream>
#include <vector>
using namespace std;

// Vector Based Queue
class MyQueue
{
private:
    vector<int> vec;
    int head;
    int tail;

public:
    MyQueue() { head = tail = -1; };
    void enqueue(int x);
    int dequeue();
    bool isEmpty();
    int size();
    void printQueue();
};

bool MyQueue::isEmpty()
{
    if (head == tail && tail == -1)
        return true;
    else
        return false;
}

void MyQueue::enqueue(int x)
{
    if (isEmpty())
    {

        head = tail = 0;
    }
    else
    {

        tail++;
    }
    vec.push_back(x);
}

int MyQueue::dequeue()
{
    int x;
    if (isEmpty())
        return -1;
    if (head == tail && tail == 0)
    {
        x = vec[head];
        vec.erase(vec.begin());
        head = tail = -1;
        return x;
    }
    else
    {
        x = vec[head];
        vec.erase(vec.begin());
        // head = vec.begin();
        return x;
    }
}

int MyQueue::size()
{
    return vec.size();
}

void MyQueue::printQueue()
{
    while (!isEmpty())
    {
        cout << dequeue() << endl;
    }
}

// int main()
// {
//     MyQueue q;
//     q.enqueue(5);
//     q.enqueue(6);
//     q.enqueue(7);
//     q.enqueue(3);
//     q.enqueue(9);
//     cout << q.isEmpty() << endl;
//     int y = q.size();
//     q.printQueue();

//     return 0;
// }