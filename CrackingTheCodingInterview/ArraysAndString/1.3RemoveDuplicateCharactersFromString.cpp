/*
	Design an algorithm and write code to remove the duplicate characters in a string
	without using any additional buffer. NOTE: One or two additional variables are fine.
	An extra copy of the array is not.
	FOLLOW UP
	Write the test cases for this method.
	
*/

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const* argv[]){
	string str;
	getline(cin, str);

	int array_chs[256];
	int tmp, i, cont_array = 0;

	for(i = 0; i < 256; i++)
		array_chs[i] = 0;

	//O(n)
	for(i = 0; i < str.length(); i++){
		tmp = str.at(i);
		if(!array_chs[tmp]){
			array_chs[tmp] = 1;
			str[cont_array++] = str[i];
		}
	}

	str = str.substr(0,cont_array);
	cout << str << endl;

	return 0;
}