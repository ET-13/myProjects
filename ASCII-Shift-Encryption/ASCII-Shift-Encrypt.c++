#include <string>
#include <iostream>
#include <vector>

int main() {
	
std::string text;
int rule;
	
std::cout << "Input string to encrypt in ASCII (no spaces): " << std::endl;
std::cin >> text;
std::cout << "Input an integer, this will shift the ASCII values by that amount: " << std::endl;
std::cin>> rule; 

  
//determine length of string
int length = text.length();
//initialize int to hold and transfer values to vector
int shift;
//initialize vector
std::vector<int> shiftvector;
//for length of string, append vector from string incrementally and shift-modify based on value of "rule"
for(int i = 0; i < length; i++){
    shift = text[i];
    shiftvector.push_back(shift+rule);
   
 } 
//clear string "text" to re-assign
 text.erase();
 //initialize char holder to fill text string through vector
 char ch;
//for every shifted number element in vector populate text string with ascii chars
 for(int i = 0; i < shiftvector.size(); i++){
	 ch = shiftvector[i];
	 text += ch;
	 
	 
}

//return ascii-encoded and shifted string
  std::cout << "Your string has been encrypted in ASCII, shifted through ASCII by the desired amount and is now returned to you in char-type..." << std::endl;
  std::cout << std::endl;
  std::cout << "Encrypted string: " << text << std::endl;
};


	
 


