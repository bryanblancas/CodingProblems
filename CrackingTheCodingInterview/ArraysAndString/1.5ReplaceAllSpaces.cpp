#include <iostream>
#include <string>

using namespace std;


//O(n)
void replaceAllSpaces(string *s){
	string str = *s;
	int spaces = 0, newlength = 0, i = 0;
	int length = str.length();

	for(i = 0; i < length; i++)
		if(str[i] == ' ')
			spaces++;

	newlength = length + spaces*2;
	str.resize (newlength);
	
	//También se copia el final de cadena '\0'
	for(i = length; i >= 0; i--){
		if(str[i] == ' '){
			str[newlength--] = '0';
			str[newlength--] = '2';
			str[newlength--] = '%';
		}
		else
			str[newlength--] = str[i];
	}

	cout << str << endl;
	*s = str;

}

int main(int argc, char const *argv[]){
	
	string str;
	getline(cin, str);

	replaceAllSpaces(&str);
	cout << str << endl;

	return 0;
}