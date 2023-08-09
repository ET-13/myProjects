
#include <iostream>
#include <vector>


using namespace std;

int main() {


    int amountselect;
    int intselect;
    
    

    std::vector <int> UnsortedArray;
    std::vector <int> HalfLeftArray;
    std::vector <int> HalfRightArray;

    

    cout << "Enter size of your array: " << endl;
    cin >> amountselect;
    cout << "Enter elements for the array one by one: " << endl;
    for(int i = 1; i<= amountselect; i++){

        cin >> intselect;
        UnsortedArray.push_back(intselect);
        
    }
    //UnsortedArray contains all elements of amount specified by user

    for(int i = 0; i < amountselect/2; i++){

        HalfLeftArray.push_back(UnsortedArray[i]);

        
    }
    //HalfLeftArray takes all elements on the 'left' side of UnsortedArray given UnsortedArray is bisected into two

    for(int i = amountselect/2; i < amountselect; i++){
        HalfRightArray.push_back(UnsortedArray[i]);
    }
    //HalfRightArray takes all elements on the 'right' side of UnsortedArray given UnsortedArray is bisected into two
    

    sort(HalfLeftArray.begin(), HalfLeftArray.end());
    sort(HalfRightArray.begin(), HalfRightArray.end());



    std::vector <int> SortedArray;
    SortedArray.insert(SortedArray.begin(), HalfLeftArray.begin(), HalfLeftArray.end());
    SortedArray.insert(SortedArray.end(), HalfRightArray.begin(), HalfRightArray.end());

    sort(SortedArray.begin(), SortedArray.end());

    cout << "Your sorted array: " << endl;
    for(int i = 0; i < amountselect; i++){
        
        cout << SortedArray[i] << ", ";

    }
    



   

















    

    

  









}
