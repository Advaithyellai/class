#include <stdio.h>
#include <stdlib.h>

typedef struct idk{
    int data;
    struct idk* left;
    struct idk* right;
} node;

node* head = NULL;

void addnode(int val) {
    if (head == NULL){
        head = malloc(sizeof(node));
        head->data = val;
        return;
    }
    node *ptr = head;
    while (1) {
        if (val>ptr->data){
            if (ptr->right == NULL) {
                ptr->right = malloc(sizeof(node));
                ptr->right->data = val;
                return;
            }
            ptr = ptr->right;
        }
        else if (val<ptr->data){
            if (ptr->left == NULL) {
                ptr->left = malloc(sizeof(node));
                ptr->left->data = val;
                return;
            }
            ptr = ptr->left;
        }
    }
}

int delete(int val){
    node *ptr = head, *prevptr;
    if (head->data == val) {
        prevptr = head->right;
        ptr = head->right;
        while(ptr->left){ptr = ptr->left;}
        ptr->left = head->left;
        head = prevptr;
        return 1;
    }
    int pos = 1;
    while (ptr) {
        if (val>ptr->data){
            prevptr = ptr;
            ptr = ptr->right;
            pos = 1;
        }
        else if (val<ptr->data){
            prevptr = ptr;
            ptr = ptr->left;
            pos = -1;
        }
        else{
            if (pos == -1) {
                if (ptr->right == NULL) {prevptr->left = ptr->left;}
                else {
                    prevptr->left = ptr->right;
                    node *ptr2 = ptr->right;
                    while(ptr2->left){ptr2 = ptr2->left;}
                    ptr2->left = ptr->left;
                }
            }
            else {
                if (ptr->left == NULL) {prevptr->right = ptr->right;}
                else {
                    prevptr->right = ptr->left;
                    node *ptr2 = ptr->left;
                    while(ptr2->right){ptr2 = ptr2->right;}
                    ptr2->right = ptr->right;
                }
            }
            return 1;
        }
    }
    return 0;
}

int search(int val) {
    node *ptr = head;
    while (ptr) {
        if (val>ptr->data){ptr = ptr->right;}
        else if (val<ptr->data){ptr = ptr->left;}
        else {return 1;}
    }
    return 0;
}

void prtsorted(node* ptr) {
    if (ptr->left) {prtsorted(ptr->left);};
    printf("%d ", ptr->data);
    if (ptr->right) {prtsorted(ptr->right);};
}

int main() {
    int choice, value;
    printf("1 - Add.\n2 - Delete.\n3 - Search.\n4 - Print As Sorted.\n5 - Quit.\n\n");
    while (1) {
        scanf("%d", &choice);
        if (choice == 1) {
            scanf("%d", &value);
            addnode(value);
        }
        else if (choice == 2) {
            scanf("%d", &value);
            (delete(value))?printf("Value %d Successfully deleted.\n", value):printf("Value %d not found.\n", value);
        }
        else if (choice == 3) {
            scanf("%d", &value);
            (search(value))?printf("Value %d found.\n", value):printf("Value %d not found.\n", value);
        }
        else if (choice == 4) {
            prtsorted(head);
            printf("\n");
        }
        else if (choice == 5) {return 1;}
        else {
            printf("Command not understood. Try again.\n");
            printf("1 - Add.\n2 - Delete.\n3 - Search.\n4 - Print As Sorted.\n5 - Quit.\n\n");
        }
    }
}