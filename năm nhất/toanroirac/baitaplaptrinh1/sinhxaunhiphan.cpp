#include <bits/stdc++.h>
using namespace std;
int check(string output) {
	int l= 0,r= output.length()-1;
	while(l <= r) {
		if(output[l] != output[r]) return 0;
		l++;
		r--;
	}
	return 1;
}
void genBinaryString(int n, string output) {
	if (output.length() == n) {
		if (check(output)) {
			for(auto x: output) {
				cout<< x;
			}
			cout <<  " ";
		}
		return;
	}
	genBinaryString(n, output + '0');
	genBinaryString(n, output + '1');
}
int main() {
	int n;
	cin >> n;
	genBinaryString(n, "");
	cout<<endl;

}
