#include<stdio.h>
void ordenar(int *s,int lng){
	int i,j,menor,pos,temp;
	for(i=0;i<lng;i++){
		menor=*(s+i);
		pos=i;
		for(j=i+1;j<lng;j++){
			if(menor>*(s+j)){
				menor=*(s+j);
				pos=j;
			}
		}
		if(pos!=i){
			temp=*(s+i);
			*(s+i)=*(s+pos);
			*(s+pos)=temp;
		}
	}
}
int main(int argc, char const *argv[]){
	int nc,nh,vah,buscador_her,op;
	int i,j,k,*s,pos_li=0,l,op1;
	scanf("%d",&nc);
	for(i=0;i<nc;i++){
		pos_li=0;
		scanf("%d",&nh);
		int hermanos[nh][2];
		int hermanos_lin[nh*2];
		for(j=0;j<nh;j++)
			for(k=0;k<2;k++){
				scanf("%d",&vah);
				hermanos[j][k]=vah;
				hermanos_lin[pos_li++]=vah;
			}
		ordenar(&hermanos_lin[0],nh*2);
		scanf("%d",&buscador_her);
		printf("Caso #%d : ",i+1);	
		for(j=0;j<buscador_her;j++){
			scanf("%d",&op);
			for(l=0;l<nh;l++)
				for(k=0;k<2;k++){
					if(hermanos[l][k]==op && k==1){
						op1=hermanos[l][0];
						break;
					}
					else if(hermanos[l][k]==op && k==0){
						op1=hermanos[l][1];
						break;
					}	
				}
			for(l=0;l<nh*2;l++)
				if(hermanos_lin[l]==op1)
					printf("%d ",l+1);
		}
		printf("\n");
	}
	return 0;
}
