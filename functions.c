#include <stdio.h>

float cmult(int int_param, float float_param) {
    float result = int_param * float_param;
    printf("C program : result from multiplying int %d and float %.1f is %.1f\n", int_param,
            float_param, result);
    return result;
}


int csum(int a, int b){
    int result = a + b;
    printf("C program : result from adding int %d and int %d is %d\n", a, b, result);
    return result;
}

int * cfun_array( int arr[3]){
    arr[1] = 100;
    printf("C program : changing second element of array to %d\n", arr[1]);
    arr[2] = arr[0] + 5;
    return arr;
}

struct myStruct { 
    char* name;
    int age;
    double mark;
}; 
  

struct myStruct * comprobar_num(struct myStruct *n) 
{
  printf("C Program : %s, %d, %f\n", n->name, n->age, n->mark);
  printf("C Program : adding 1 year old\n");
  n->age=n->age + 1;
  return n;
}
