#include<iostream>
using namespace std;
int add(int a, int b)
{
    return a + b;
}
int sub(int a, int b){
    return a - b;
}

int main()
{
    int a, b, choice;
    cout<<"enter first number: ";
    cin>>a;
    int b;
    cout<<"enter second number: ";
    cin>>b;
    
    cout<<"\nSelect operation:\n";
    cout<<"1. Addition\n";
    cout<<"2. Subtraction\n";
    cout<<"Enter your choice (1 or 2): ";
    cin>>choice;
    
    if(choice == 1)
    {
        cout<<"\nResult: "<<a<<" + "<<b<<" = "<<add(a, b)<<endl;
    }
    else if(choice == 2)
    {
        cout<<"\nResult: "<<a<<" - "<<b<<" = "<<sub(a, b)<<endl;
    }
    else
    {
        cout<<"\nInvalid choice!"<<endl;
    }
    
    return 0;
}