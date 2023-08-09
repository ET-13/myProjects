#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {

    int KeyLength;
    int KeyNumber;
    int Counter1=0;
    int Counter2=0;
    int Counter3=0;

    cout << "Enter number,amount of elements will be created up to that length" << endl;
    cin >> KeyLength;
    cout << "Of numbers within that length (0 exclusive) input an integer you'd like the search algorithm to find" << endl;
    cin >> KeyNumber;

    //array of elements

    std::vector <int> ElemArray;

    for(int i = 1; i <= KeyLength; i++){
        ElemArray.push_back(i);
    }





//divide into third, search backward to 1

    for(int i = KeyLength/3; i > 0; i--){

        cout << "Program guesses " << i << endl;
        Counter1++;
        

        if(i==KeyNumber){
            cout <<"Your number was " << ElemArray[i-1] << endl;
            cout <<"It took: " << Counter1 << " tries." << endl;
            break;
            EXIT_SUCCESS;
        } 
        else if (Counter1>=KeyLength/3){
            //if not found, divide into half, search backward to start of given third-section
            for(int j = KeyLength/2; j > KeyLength/3 ;j--){
                cout << "Program guesses " << j << endl;
                Counter2++;
                if(j==KeyNumber){
                    cout<<"Your number was " << ElemArray[j-1] << endl;
                    cout <<"It took: " << Counter2 + Counter1 << " tries." << endl;
                    break;
                    EXIT_SUCCESS;
                }

                else if ((Counter2+Counter1)>=KeyLength/2){
                    //if not found, search backward from last element to start of given half-section
                    for(int k = KeyLength; k > KeyLength/2; k--){
                        cout << "Program guesses " << k << endl;
                        Counter3++;
                        if(k==KeyNumber){
                            cout<<"Your number was " << ElemArray[k-1] << endl;
                            cout<<"It took: " << Counter3 + Counter2 + Counter1 << " tries." << endl;
                            

                            break;
                            EXIT_SUCCESS;
                        }
                    }
                }
            }
        } 


    }

    return 0;
}