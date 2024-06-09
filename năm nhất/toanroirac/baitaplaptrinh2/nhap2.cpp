#include<bits/stdc++.h>
using namespace std;
int n,k,a[21],X[21];
vector<string> v;
void Try(int i,int bd){
	for(int j=bd;j<=n;j++){
		if(a[j] > X[i-1]){
			X[i] = a[j];
			if(i == k){
				string s = "";
				for(int u=1;u<=k;u++){
					s += to_string(X[u]) + " ";
				}
				v.push_back(s);
			}
			Try(i+1,j+1); 
		}
	}
}
int main(){
	int n,k,a[21],X[21];
	vector<string> v;
	cin >> n >> k;
	for(int i=1;i<=n;i++) cin >> a[i];
	Try(1,1);
	for(auto it : v){
		cout << it << endl;
	}
}