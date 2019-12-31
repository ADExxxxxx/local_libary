#include<iostream>
#include<stdio.h>
#include<string>
#include<sstream>
#include<fstream>
#include<vector> 
#include<iomanip> 
#include<stack> 
#include<list>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
int num = 0;
class point {
public:
	int x;
	int y;
	point(int a, int b) {
		x = a;
		y = b;
	}
};
//检查同行，同列，同区域内是否含有此数 
bool check(int a[9][9], int i, int j, int k) {
	for (int x = 0; x <= 8; x++) {
		if (a[x][j] == k) {
			return false;
		}
	}
	for (int x = 0; x <= 8; x++) {
		if (a[i][x] == k) {
			return false;
		}
	}
	for (int p = (i / 3) * 3; p < (i / 3) * 3 + 3; p++) {
		for (int q = (j / 3) * 3; q < (j / 3) * 3 + 3; q++) {
			if (a[p][q] == k) {
				return false;
			}
		}
	}
	return true;
}

void out(int a[9][9]) {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << a[i][j] << " ";
		}cout << endl;
	}
}


void solve(int a[9][9], vector<point>& v, int cur) {
	if (cur == v.size()) {
		out(a);
		cout << endl;
		return;
	}
	for (int k = 1; k <= 9; k++) {
		if (check(a, v[cur].x, v[cur].y, k)) {
			a[v[cur].x][v[cur].y] = k;
			solve(a, v, cur + 1);
			a[v[cur].x][v[cur].y] = 0;
		}
	}
	return;
}
int main() {
	int a[9][9];
	vector<point>v;//记录要填空的坐标 

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> a[i][j];
			if (a[i][j] == 0) {
				point p = point(i, j);
				v.push_back(p);
			}
		}
	}
	solve(a, v, 0);
	return 0;
}