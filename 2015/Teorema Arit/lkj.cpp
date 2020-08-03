#include <stdio.h>
#include <time.h>

int primo(long long f);
void fact_primos(long long a);

int main(){
	clock_t w=clock();
	long long a;
	while(scanf("%lld",&a)!=EOF){
		printf("%lld: ",a);
		fact_primos(a);
		printf("\n");
	}
	printf("time: %f",(double)(clock()-w)/CLOCKS_PER_SEC);
}

void fact_primos(long long a){
	long long i;
	if(primo(a)==1){
		printf("%lld",a);
		return;
	}
	for(i=2;i<a;i++){
		if(primo(i)==1 && a%i==0){
			printf("%lld ",i);
			break;
		}
	}
	fact_primos(a/i);
}

int primo(long long f){
	long long i,r=1;
	while(r*r<=f)
		r++;
	r--;
	for(i=2;i<=r;i++)
		if(f%i==0)
			return 0;
	return 1;	
}
