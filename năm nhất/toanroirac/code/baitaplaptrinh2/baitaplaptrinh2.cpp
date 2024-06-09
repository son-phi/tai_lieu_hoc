#include <bits/stdc++.h>
using namespace std;

int n, k, Arr[100], X[100];
vector<string> res;

void Input() {
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
		cin >> Arr[i];
}

void Try(int i, int bd) {
	for (int j = bd; j <= n; j++)
		if (Arr[j] > X[i - 1]) {
			X[i] = Arr[j];
			if (i == k) {
				string s = "";''
				for (int u = 1; u <= k; u++)
					s += to_string(X[u]) + " ";
				res.push_back(s);
			}
			Try(i + 1, j + 1);
		}
}

void Output() {
	for (auto it : res)
		cout << it << endl;
}
.
int main() {
	Input();
	Try(1, 1);
	Output();
}