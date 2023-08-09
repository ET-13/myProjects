#include <iostream>
#include <string>
#include <cmath>
using namespace std;



int main() {

    int polydegree;

    cout << "[Polynomial Derivative Auto-Taker]" << endl;
    cout << endl;
    cout << "Degree of Polynomial is? (4th Degree or lower)" << endl;
    cout <<"(Hint... Highest exponent):" << endl;
    cin >> polydegree;

    float coefficient[4];

    cout <<"Type each constant of the Polynomial (lowest degree to highest): " << endl;
    for(int i = 0; i <= polydegree; i++){
        cout <<"Coefficient " << i + 1 << ": ";
        cin >> coefficient[i];
    }



   

    cout<<"Your Polynomial is: " << endl;
    
    for(int i = 0; i <= polydegree; i++){
        if(i==0){
            cout << coefficient[i] << " + "; //Constant
        }
        else if (i==polydegree) {
            cout << coefficient[i] << "X^" << i << endl; //Last Co-ef and degree
        }
        else {
            cout << coefficient[i] << "X^" << i << " + "; //Each Co-ef and degree
        }
        


    }

    float x = 1; //first derivative constant multiplier
    float y = 2;//first degree term derivative multiplier
    float z = 3;//second degree term derivative multiplier
    float w = 4;//third degree term derivative multiplier
  



    

    float derivativeconstant = 0.0;
    float coeffirst = 0.0;
    float coefsecond = 0.0;
    float coefthird=0.0;
  
    


    for (int i = 0; i <= 1; i++){
        derivativeconstant += coefficient[i] * pow(x, i);
        
    }
    for(int i = 0; i <= 1; i++){
        coeffirst = y*coefficient[2];
        
    }
    for(int i = 0; i <=1; i++){
        coefsecond = z*coefficient[3];
        
    }
    for(int i =0; i<=1; i++){
        coefthird=w*coefficient[4];
    }
 

    cout << endl;

    if(polydegree==1){
        cout << "Derivative is: " << derivativeconstant;
    }
    if(polydegree==2){
        
        cout << "Derivative is: " << derivativeconstant << " + " << coeffirst << "X" << endl;
    }
    if(polydegree==3){

        cout << "Derivative is: " << derivativeconstant << " + " << coeffirst << "X" << " + " << coefsecond << "X^2" << endl;
    }
    if(polydegree==4){

        cout << "Derivative is: " << derivativeconstant << " + " << coeffirst << "X" << " + " << coefsecond << "X^2" << " + " << coefthird << "X^3" << endl;

    }
  

    return(0);

    


    



   


   



    


    
   
}