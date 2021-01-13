/*
7
4 	First spy spies number 4
3 	Second spies number 3
2 	
5
6
1
3


array[]

0 1 2 3 4 5 6

4 3 2 5 6 1 3


4 5 6 1

3 2

2 3

5 6 1 4 

... 

a = 4
b = 4

aux = 3*/


public static int fuckingSpies(int array[]){
	
	int max_size = 0;

	SC O(1)
	TC O(n^2)
	for(int i = 0; i < array.length; i++){

		int b = array[a-1];
		aux = 1;
		while(array[i] != b){
			aux++;
			b = array[b-1];
		}

		max_size = max(max_size, aux);

	}

	return max_size;
}




