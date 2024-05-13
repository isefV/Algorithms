#include <math.h>
#include <stdio.h>
#include <iostream>

float cb_square(int num)
{
    return num * num;
}

float cb_cube(int num)
{
    return num * num * num;
}

float cb_square_root(int num)
{
    return sqrt(num);
}

float calc(int num, float (*op)(int))
{
    return op(num);
}

int cmp(char* s1,char* s2,int cnt){
    char* c1=s1;
    char* c2=s2;

    while (cnt-->0)
    {
        if(*c1++==*c2++){
            printf("%c", c1[-1]);
        }
    }
    return 0;
}

void doubleastrick(char*** G){
    std::cout<<"***G:"<<G<<"\t**G:"<<*G<<"\t*G:"<<**G<<"\tG:"<<***G<<std::endl;
    **G+=1;
    std::cout<<"***G:"<<G<<"\t**G:"<<*G<<"\t*G:"<<**G<<"\tG:"<<***G<<std::endl;
    *G-=1;
    std::cout<<"***G:"<<G<<"\t**G:"<<*G<<"\t*G:"<<**G<<"\tG:"<<***G<<std::endl;
    G+=1;
    std::cout<<"***G:"<<G<<"\t**G:"<<*G<<"\t*G:"<<**G<<"\tG:"<<***G<<std::endl;
}

int main()
{
    char c[3]={'V','s','A'};
    char d[3]={'f','g','a'};
    char* cc=c;
    char* dd=d;
    char** ccc[2];
    ccc[0]=&cc;               
    ccc[1]=&dd;               

    //dd=&dd;
    doubleastrick(ccc);
    //printf("\ncmp:\t%d", cmp(c,d,4));
    // printf("cube:\t%.2f\n", calc(5, cb_cube));
    // printf("sqrt:\t%.2f\n", calc(5, cb_square_root));

    return 0;
}