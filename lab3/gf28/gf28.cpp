#include<iostream>
#include<iomanip>
using namespace std;

int gfadd(int a,int b) {
	return a^b;
}

int gfmul(int a, int b) {
	int res = 0;
	while (b) {
		if (b & 1) {
			res ^= a;
		}
		b >>= 1;
		a <<= 1;
		if (a > 255)
			a ^= 283;
	}
	return res;
}

int table(int grp[], int inv[], int g = 3) {
	grp[0] = 0;
	grp[1] = g;
	for (int i = 2; i < 256; ++i) {
		grp[i] = gfmul(grp[i - 1], g);	
	}
	inv[0] = 0;
	inv[1] = 1;
	for (int i = 1; i < 128; ++i) {
		inv[grp[i]] = grp[255 - i];
		inv[grp[255 - i]] = grp[i];
	}
	return 1;
}//set up g^x_table and inverse_table

int inver(int x,int inv[]) {
	return inv[x];
}

int discreteg(int x,int grp[]) {
	int i = 0;
	while (i <= 256) {
		if (grp[i] == x)break;
		++i;
	}
	return i;
}

void Sbox(int inv[]) {
	int sbox[256] = { 0 };
	unsigned char btmp;
	for (int i = 0; i < 256; ++i) {
		btmp = (unsigned char)inv[i];
		// bi' = bi ^ b(i+4) ^ b(i+5) ^ b(i+6) ^ b(i+7) ^ {64}
		sbox[i] = btmp^_rotl8(btmp, 1) ^ _rotl8(btmp, 2) ^ _rotl8(btmp, 3) ^ _rotl8(btmp, 4) ^ 0x63;	
		if (i % 16 == 0)cout << endl;
		cout << setw(3) << sbox[i];
	}
}

int main() {
	int g, x, y;
	int grp[256] = { 0 };//table of g^x
	int inv[256] = { 0 };//table of x's inverse
	table(grp, inv);
	while (1) {
		/*cout << "input x, y (all hex): ";
		cin >> hex >> x >> hex >> y;
		cout << "x + y = " << hex << gfadd(x, y) << endl;

		cout << "input x, y (all hex): ";
		cin >> hex >> x >> hex >> y;
		cout << "x * y = " << hex << gfmul(x, y) << endl;

		cout << "input x(hex): ";
		cin >> hex >> x;
		cout << "x * y = 1  solution: y = " << hex << inver(x, inv) << endl;*/

		cout << "input g, x (all dec): ";
		cin >> g >> x;
		table(grp, inv, g);
		cout << "g * y = x  solution: y = " << hex << discreteg(x, grp) << endl;
		
		cout << "\nAES's S-Box";
		Sbox(inv);
		cout << endl << endl;
	}
	return 0;
}