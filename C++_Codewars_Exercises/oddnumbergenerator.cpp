#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    int mynumber; //given an input
    cin >> mynumber;
    
    for (int i = 1; i <= mynumber; i++) { //loop through range of input starting at one
        
        if(i % 2 != 0)
        {   
            
            cout << i << ""; //return all odd numbers in that range
              
        }

        
    
    }

    return 0;
}