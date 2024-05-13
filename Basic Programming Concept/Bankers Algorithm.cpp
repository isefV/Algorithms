#include <iostream>
#include <string>

void getData(int *procSize , int *resSize);
void getData(int *procSize , int *resSize ,int *resData, std::string *procName , std::string *resName , int *alloc , int *max);
template<class U> void print(std::string str, U data);
template<class U> void get(U *data);

int main(){

    int processSize=3,resourceSize=3;

    getData(&processSize,&resourceSize);

    int resourceData[resourceSize] , allocation[processSize][resourceSize] , maximum[processSize][resourceSize];
    std::string processName[processSize],resourceName[resourceSize];

    getData(&processSize,&resourceSize,resourceData,processName,resourceName,allocation,maximum);

    return 0;
}


void getData(int *procSize , int *resSize){

    print("Enter Number of Process:",false);
    get(&procSize);


    print("\nEnter Number of Resource:",false);
    get(&resSize);

}

void getData(int *procSize , int *resSize ,int *resData, std::string *procName , std::string *resName , int *alloc , int *max){
    
    for(int i=0 ; i<*procSize ; i++){
        print("\nEnter Name of Process ", i+1);
        print(" :", false);
        get(&procName[i]);
    }

    for(int i=0 ; i<*resSize ; i++){
        print("\nEnter Name of Resource ", i+1);
        print(" :", false);
        get(&resName[i]);
        print("\nEnter Count of Resource ", &resName[i]);
        print(" :", false);
        get(&resData[i]);
    }

    for(int i=0 ; i<*procSize ; i++){
        for(int j=0 ; j<*resSize ; j++){
            print("\nEnter Allocation of ", &resName[j]);
            print(" by", &procName[i]);
            print(" :", false);
            get(&alloc[i][j]);

            print("\nEnter Max of ", &resName[j]);
            print(" by", &procName[i]);
            print(" :", false);
            get(&max[i][j]);
        }
    }
}

template<class U> void print(std::string str, U data){
    std::cout<<str;
    if(data)
        std::cout<<data;
}

template<class U> void get(U *data){
    std::cin>>*data;
}