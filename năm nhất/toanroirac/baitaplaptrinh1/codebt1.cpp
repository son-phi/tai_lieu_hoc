#include<bits/stdc++.h>
using namespace std;
int n,m,a[10000],final;
void ktao(){
	for(int i=1;i<=m+n;i++){
		a[i]=0;
	}
}
void sinh(){
	int i=m+n;
	while(i>=0 && a[i]==1){
		a[i]=0;
		i--;
	}
	if(i==0) final=0;
	else a[i]=1;
}
int check(){
	int d=0;
	for(int i=1;i<=m+n;i++){
		if(a[i]==1){
			d++;
		}
	}
	if(d==n) return 1;
	return 0;
}
void in(){
	if(check()){
		int x=0 , y=0;
		for(int i=1;i<=m+n;i++){
			if(a[i]==0){
				x++;
				cout << "R" << x << " ";
			}
			else{
				y++;
				cout << "U" << y << " ";
			}
		}
		cout << endl;
	}
}
int main(){
	cin >> n >> m;
	final=1;
	ktao();
	while(final){
		sinh();
		in();
	}
}