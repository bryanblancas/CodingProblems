#include <stdio.h>
#include <stdlib.h>
#define const 4
int main(){

	int tablero[const][const];
	int i,j,k,l,o;
		
	for(i=0;i<const;i++)
		for(j=0;j<const;j++){
			printf("Introduce el valor de [%d][%d]:\n",i,j);
			scanf("%d",&o);
			tablero[i][j]=o;
		}
	
	for(i=0;i<const;i++){
		for(j=0;j<const;j++)	
			printf("%d ",tablero[i][j]);
		printf("\n");
	}
	
	//checar coindicencias horizontales
	for(i=0;i<const;i++){
		for(j=0;j<const;j++){
			if(tablero[i][j]==1){	
				for(k=j+1;k<const;k++){
					if(tablero[i][j]==tablero[i][k]){
						printf("(%d,%d)-(%d,%d)\n",i,j,i,k);
					}
				}
			}
		}
	}
	//checar coindicencias verticales
	for(i=0;i<const;i++){
		for(j=0;j<const;j++){
			if(tablero[i][j]==1){	
				for(k=i+1;k<const;k++){
					if(tablero[i][j]==tablero[k][j]){
						printf("(%d,%d)-(%d,%d)\n",i,j,k,j);
					}
				}
			}
		}
	}
	//checar coindicencias diagonales
	for(i=0;i<const;i++){
		for(j=0;j<const;j++){
			if(tablero[i][j]==1){	
				for(k=i+1,l=j+1;k<const,l<const;k++,l++){
					if(tablero[i][j]==tablero[k][l]){
						printf("(%d,%d)-(%d,%d)\n",i,j,k,l);
					}
				}
				for(k=i-1,l=j+1;l<const;k--,l++){
					if(tablero[i][j]==tablero[k][l]){
						printf("(%d,%d)-(%d,%d)\n",i,j,k,l);
					}
				}
				for(k=i+1,l=j-1;k<const;k++,l--){
					if(tablero[i][j]==tablero[k][l]){
						printf("(%d,%d)-(%d,%d)\n",i,j,k,l);
					}
				}
			}
		}
	}
	
	return 0;		
}
