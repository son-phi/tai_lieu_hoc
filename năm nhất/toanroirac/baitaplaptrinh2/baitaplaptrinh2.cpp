#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define FOR(i,r,n) for(int i=r; i<n; ++i)
int n, k;
int a[21], x[21];
vector<string> v; 
bool ok;
 void setup() {
	v.clear();
	FOR(i, 1, k + 1) {
		x[i] = i;
	}
}
 void sinh() {
	int i = k;
	string tmp = "";
	FOR(i, 1, k+1) {
		if (a[x[i]] > a[x[i - 1]]) tmp += to_string(a[x[i]]);
	}
	if (tmp.size() == k) v.pb(tmp);
	while (i >= 1 and x[i] == n - k + i) {
		--i;
	}
	if (i == 0) ok = false;
	else {
		x[i]++;
		FOR(j, i + 1, k + 1) {
			x[j] = x[j - 1] + 1;
		}
	}
}
 
void solve() {
	cin >> n >> k;
	FOR(i, 1, n + 1) cin >> a[i];
	setup();
	ok = true;
	while (ok) {
		sinh();
	}
	for (string x : v) {
		cout << x << endl;
	}
}
 
int main() {
		solve();
}