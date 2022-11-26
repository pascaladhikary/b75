/*
notes:  hold two rptr, because we add at r+1, but access at r
*/
#include <stdbool.h>
typedef struct {
    int* arr;
    int size, n, l, r0, r1;
} MyCircularQueue;

bool myCircularQueueIsFull(MyCircularQueue* obj);
bool myCircularQueueIsEmpty(MyCircularQueue* obj);

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue* q = calloc(1, sizeof(MyCircularQueue));
    
    q->arr = calloc(1, sizeof(int));
    q->size = k;
    return q;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (myCircularQueueIsFull(obj)) 
        return false;
    
    obj->arr[obj->r0 = obj->r1] = value;
    obj->r1 = (obj->r1 + 1) % (obj->size);
    obj->n++;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj))
        return false;
    
    obj->l = (obj->l + 1) % (obj->size);
    obj->n--;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    return (myCircularQueueIsEmpty(obj)) ? -1 : obj->arr[obj->l];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    return (myCircularQueueIsEmpty(obj)) ? -1 : obj->arr[obj->r0];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->n == 0;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->n == obj->size;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->arr);
    free(obj);
}