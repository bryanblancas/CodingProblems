/*

	Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
	five characters, including the null character.)

*/

#include <iostream>
#include <string>

using namespace std;

void reverseString(string *s){
	string str = *s;
	int str_len = str.length();
	int str_m_len = (int) str_len / 2;

	int i, j = 0;
	//O(n/2)
	for(i = str_len-1; i >= str_m_len; i--){
		char ch = str[j];
		str[j] = str[i];
		str[i] = ch;
		j++;
	}

	*s = str; 
}


int main(int argc, char const* argv[]){

	string str;
	getline(cin, str);

	cout << str << endl;

	// O(n)
	reverseString(&str);

	cout << str << endl;


}