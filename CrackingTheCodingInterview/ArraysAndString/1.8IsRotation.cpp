/*
	Assume you have a method isSubstring which checks if one word is a substring of
	another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
	only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
*/

#include <iostream>
#include <string>

using namespace std;

string rotate(string cad, int len, int i){
	return cad.substr(i, len-i) + cad.substr(0, i);
}

bool isSubstring(string cad1, string cad2){
	if (cad1.find(cad2) != std::string::npos)
	    return true;
	return false;
}

// O(n???)
bool is_rotation(string rot, string cad){
	int len_cad = cad.length();
	int len_rot = rot.length();

	if(len_cad != len_rot)
		return false;
	if(isSubstring(rot, cad))
		return true;

	string aux = "";
	for(int i = 1; i < len_rot; i++){
		aux = rotate(rot, len_rot, i);
		if(isSubstring(aux, cad))
			return true;
	}

	return false;
}

int main(int argc, char const* argv[]){

	cout << is_rotation("lyon", "only") << endl;
	cout << is_rotation("lnyo", "only") << endl;
	cout << is_rotation("lyoni", "onlyi") << endl;
	cout << is_rotation("an israelbry", "bryan israel") << endl;
	cout << is_rotation("hola mundo cruel", "cruelhola mundo ") << endl;

}