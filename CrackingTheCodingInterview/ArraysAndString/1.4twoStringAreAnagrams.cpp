#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <iterator>

using namespace std;


//O(n)
int areAnagrams(string str1, string str2){
	map<char, int> ht;
	map<char, int>::iterator itr;

	if(str1.length() != str2.length())
		return 0;

	for(char ch: str1){
		if(ht.find(ch) != ht.end())
			ht[ch] += 1;
		else
			ht[ch] = 1;
	}

	for(char ch: str2){
		if(ht.find(ch) != ht.end()){
			ht[ch] -= 1;
			if(ht[ch] < 0)
				return 0;
		}
		else
			return 0;
	}

	for(itr = ht.begin(); itr != ht.end(); itr++)
		if(itr -> second != 0)
			return 0;

	return 1;
}

//O(nlogn)
int areAnagrams_sorting(string str1, string str2){
	std::sort(str1.begin(), str1.end());
	std::sort(str2.begin(), str2.end());
	if(str1 == str2)
		return 1;
	return 0;

}

int main(int argc, char const *argv[]){
	
	string str1, str2;
	getline(cin, str1);
	getline(cin, str2);


	if(areAnagrams(str1,str2))
		cout << "YES" << endl;
	else
		cout << "NO" << endl;

	
	if(areAnagrams_sorting(str1,str2))
		cout << "YES" << endl;
	else
		cout << "NO" << endl;


	return 0;
}