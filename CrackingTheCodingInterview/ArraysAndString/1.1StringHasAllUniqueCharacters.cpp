/*

	Implement an algorithm to determine if a string has all unique characters. What if you
	can not use additional data structures?

*/

#include <iostream>
#include <string>
#include <map>

using namespace std;

int hasAllUniqueCharacters_withoutDataStructure(string str){
	int i,j;
	char ch;

	for(i = 0; i < str.length(); i++){
		ch = str[i];
		for(j = i+1; j < str.length(); j++)
			if(ch == str[j]){
				return 0;
			}
	}
	return 1;

}

int hasAllUniqueCharacters_withHashmap(string str){
	map<char, int> m;

	for(char ch : str){
		if(m.find(ch) != m.end()){
			return 0;
		}
		else m[ch] = 1;
	}
	return 1;

}


int hasAllUniqueCharacters_withArray(string str){
	int chs[255];
	int i, j;
	for(j = 0; j < str.length(); j++){
		i = str.at(j);
		if(chs[i] == 1)
 			return 0;
		chs[i] = 1;
	}
	return 1;

}

int main(int argc, char const *argv[]){

	string str;
	getline(cin, str);


	//WITHOUT DATA STRUCTURE  O(n²)
	/*
	if(hasAllUniqueCharacters_withoutDataStructure(str))
		cout << "True" << endl;
	else
		cout << "False" << endl;
	*/


	//WITH DATA STRUCTURE O(nlog n)
	/*
	if(hasAllUniqueCharacters_withHashmap(str))
		cout << "True" << endl;
	else
		cout << "False" << endl;
	*/

	
	//WITH ARRAY O(n)
	
	if(hasAllUniqueCharacters_withArray(str))
		cout << "True" << endl;
	else
		cout << "False" << endl;	
	

	return 0;
}