/*

	Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
	column is set to 0.

*/

#include <iostream>
#include <vector>

using namespace std;

void fillMatrix(int **m, int M, int N){
	srand(time(NULL));

	int i, j;
	for(i = 0; i < M; i++)
		for(j = 0; j < N; j++)
			m[i][j] = rand()%10;
}

void printMatrix(int **m, int M, int N){
	int i, j;
	for(i = 0; i < M; i++){
		for(j = 0; j < N; j++){
			cout << m[i][j];
			cout << " ";
		}
		cout << endl;
	}
}

int main(int argc, char const *argv[]){
	
	int M, N, i , j;
	vector<int> rows, columns;
	cin >> M;
	cin >> N;

	int **m = new int*[M];
	for(i = 0; i < M; i++)
		m[i] = new int[N];
	
	fillMatrix(m,M,N);
	printMatrix(m,M,N);

	//O(M*N)

	for(i = 0; i < M; i++)
		for(j = 0; j < N; j++)
			if(m[i][j] == 0){
				rows.push_back(i);
				columns.push_back(j);
			}

	for(int row: rows)
		for(i = 0; i < N; i++)
			m[row][i] = 0;

	for(int column: columns)
		for(i = 0; i < M; i++)
			m[i][column] = 0;

	cout << endl;
	printMatrix(m,M,N);

	return 0;
}