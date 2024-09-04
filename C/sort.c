#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

char Algs[5][10] = {"bubble", "quick", "selection", "insertion", "merge"}; // "all"
char Algorithm[] = "all";
int len = 10000;
int max_val = 100000;
int verbose = 0;

void bubble(int arr[], int len) {
    // time complexity = O(len^2)
    for (int j = len-1; j>0; j--) {
            for (int i = 0; i<j; i++) {
                if (arr[i] > arr[i+1]) {
                    int x = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = x;
                }
            }
    }
}

void selection(int arr[], int len) {
    // time complexity = O(len^2)
    for (int i = 0; i < len; i++) {
        int minval[2];
        for (int j = i; j<len; j++) {
            if ((arr[j] < minval[0]) || (i == j)) {
                minval[0] = arr[j];
                minval[1] = j;
            }
        }
        arr[minval[1]] = arr[i];
        arr[i] = minval[0];
    }
}

void quick(int arr[], int low, int high) {
    if (low+1 < high) {
        int pivot = arr[high-1];
        int j = low;
        int i;
        for (i = low; i<high-1; i++) {
            if (arr[i] < pivot) {
                int key = arr[j];
                arr[j] = arr[i];
                arr[i] = key;
                j++;
            }
        }

        int k = arr[j];
        arr[j] = pivot;
        arr[high-1] = k;
        quick(arr, low, j);
        quick(arr, j+1, high);
    }
}

void combine(int arr[], int low, int mid, int high) {
    int arr2[high-low];
    int j = low;
    int k = mid;
    int i;
    for (i = 0; i<high-low; i++) {
        if (arr[j] < arr[k]) {
            arr2[i] = arr[j];
            j++;
        }
        else {
            arr2[i] = arr[k];
            k++;
        }
        if ((j==mid) || (k==high)) { break; }
    }

    i++;
    for (int l = j; l<mid; l++) {
        arr2[i] = arr[l];
        i++;
    }
    for (int m = k; m<high; m++) {
        arr2[i] = arr[m];
        i++;
    }
    for (int n = low; n < high; n++) {
        arr[n] = arr2[n-low];
    }
}

void merge(int arr[], int low, int high) {
    if (low+1 < high) {
        int mid = (low+high)/2;
        merge(arr, low, mid);
        merge(arr, mid, high);
        combine(arr, low, mid, high);
    }
}

void insertion(int arr[], int len) {
    // time complexity = O(n) in best case
    // time complexity = O(n^2) in worst case and average
    for (int i = 0; i < len; i++) {
        int j = i;
        while ((j > 0) && (arr[j] < arr[j-1])) {
            int k = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = k;
            j--;
        }
    }
}

void body(int arr[], char Alg[]) {
    printf("-------------------------\n");
    printf("Algorithm being used: %s", Alg);

    int start = time(NULL);

    if (((strcmp(Algorithm, "all") != 0) || (strcmp(Alg, "all") == 0)) && (verbose)){
        printf("\n\nBefore sorting: (");
        for (int i = 0; i < len-1; i++) {
            printf("%d, ", arr[i]);
        }
        printf("%d)", arr[len-1]);
    }
    
    if (strcmp(Alg, "all") == 0) {
        printf("\n\n");
        int lenalgs = sizeof(Algs)/sizeof(Algs[0]);

        for (int algc = 0; algc<lenalgs; algc++) {
            body(arr, Algs[algc]);
        }
    }
    else if (strcmp(Alg, "bubble") == 0) {bubble(arr, len);}
    else if (strcmp(Alg, "selection") == 0) {selection(arr, len);}
    else if (strcmp(Alg, "insertion") == 0) {insertion(arr, len);}
    else if (strcmp(Alg, "quick") == 0) {quick(arr, 0, len);}
    else if (strcmp(Alg, "merge") == 0) {merge(arr, 0, len);}
    else {
        printf("\n\nValueError:\nThe algorithm passed is invalid. Change the algorithm and try again.\n\n");
        return;
    }
    
    int fail = 0;
    if (((strcmp(Algorithm, "all") != 0) || (strcmp(Alg, "all") == 0)) && (verbose)) {
        printf("\nAfter sorting: (");
        
        for (int i = 0; i < len-1; i++) {
            if (arr[i] > arr[i+1]) { fail = 1; }
            printf("%d, ", arr[i]);
        }
        printf("%d)", arr[len-1]);
    }
    else {
        for (int i = 0; i < len-1; i++) {
            if (arr[i] > arr[i+1]) {
                fail = 1;
                break;
            }
        }
    }

    int end = time(NULL);
    printf("\nTime taken: %d seconds", end-start);

    if (fail == 1) {
        printf("\n\nYou are a failure.\n\n");
        exit(0);
    }
    else { printf("\n\nSorting is successful.\n"); }
    printf("-------------------------\n");
}

int main() {
    int arr[len]; //{27, 21, 76, 17, 96, 13, 7, 56, 14, 15};
    unsigned seed = time(0);
    for (int i = 0; i<len; i++){
        int k = rand_r(&seed) % max_val;
        arr[i] = k;
    }

    body(arr, Algorithm);
}