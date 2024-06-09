#include<bits/stdc++>
using namespace std
void Try(int i){ // to hop chap k cua n 
	for(int j = X[i-1]+1,j<=n-k+i;j++){
		X[i]= j;
		if (i==k){
			result();
		}
		else Try(i+1);
	}
}

int main(){
	int n;cin>>n;
	
}