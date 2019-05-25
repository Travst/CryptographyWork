	//v2.0	not using the table
#include<iostream>
#include<iomanip>
#define unschar unsigned char
#define unshort unsigned short
using namespace std;
unschar SBox[16][16];

unshort GFadd(unshort a, unshort b) {
	return a^b;
}//addition and substration are the same

unshort GFmul(unshort a, unshort b) {
	unshort res = 0;
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

int polyorder(unshort poly) {
	for (int i = 0; i < 16; ++i)
		if (!(poly >> (i + 1)))
			return i;
	return 16;
}
unshort GFdiv(unshort a, unshort b, unshort &rem) {
	if (b == 0) {
		cout << "fault operation: divided zero\n";
		return -1;
	}
	if (a < b) {
		rem = a;
		return 0;
	}
	int digree = polyorder(a) - polyorder(b);
	unshort tmp = b << digree;
	a = a ^ tmp;
	return (1 << digree) | GFdiv(a, b, rem);
}

unshort GFegcd(unshort a, unshort b, unshort &x, unshort &y) {
	if (b == 0) {
		x = 1;
		y = 0;
		return a;
	}
	unshort tmp = 0, tmp2 = 0;
	GFdiv(a, b, tmp);// tmp = a % b
	unshort ans = GFegcd(b, tmp, x, y);
	tmp = x;
	x = y;
	y = tmp ^ GFmul(GFdiv(a, b, tmp2), y);// y = tmp - a / b *y
	return ans;
}
unshort inv(unshort a) {
	unshort x, y, p = 283;
	if (GFegcd(a, p, x, y) == 1) {// ax + my = p	
		/*
		unshort tmp, ans;
		GFdiv(x, p, tmp);//	tmp = a % p
		tmp = GFadd(tmp, p);//	tmp += p
		GFdiv(tmp, p, ans);//	ans = tmp % p
		return ans;//	return (x%p + p)%p
		*/
		return x;
	}
	return p;
}//¢ñ
unshort GFinv(unshort a) {
	if (a == 0) {
		return 0;
	}
	unshort p = 0x11b, n = 0x11b;//283
	unshort r0 = 1, r1 = 0, tmp;
	unshort q = 0, d = a;
	while (n) {
		q = GFdiv(d, n, tmp);
		d = n;
		n = tmp;
		tmp = r0^GFmul(q, r1);	//	r0 - q * r1
		r0 = r1;
		r1 = tmp;
	}
	unshort x = 0;
	GFdiv(GFdiv(r0, d, tmp), p, x);	// x = (r0 / d) % p
	return x;
}//¢ò

unshort Discrelog(unshort g, unshort x) {
	if (g == 0 || (g == 1 && x != 1)) {
		cout << "no solution\n";
		return -1;
	}
	unshort y = 0;
	unshort gy = 1;
	while (gy != x) {
		gy = GFmul(gy, g);
		++y;
	}
	return y;
}

void Initbox() {
	for (int i = 0; i < 16; ++i)
		for (int j = 0; j < 16; ++j)
			SBox[i][j] = GFinv((i << 4) | j);
}
void Tranbox() {
	unschar btmp;
	for (int i = 0; i < 16; ++i)
		for (int j = 0; j < 16; ++j) {
			btmp = SBox[i][j];
			// bi' = bi ^ b(i+4) ^ b(i+5) ^ b(i+6) ^ b(i+7) ^ {63}
			SBox[i][j] = btmp ^ _rotl8(btmp, 4) ^ _rotl8(btmp, 3) ^ _rotl8(btmp, 2) ^ _rotl8(btmp, 1) ^ 0x63;
		}
}
void Dispbox() {
	Initbox();
	Tranbox();
	cout << "\nAES's S-Box:\n";
	for (int i = 0; i < 16; ++i) {
		for (int j = 0; j < 16; ++j)
			cout << setw(3) << hex << (int)SBox[i][j];
		cout << endl;
	}
}

int main() {
	unshort a = 0x2, b = 0x4, x = 0x05, g = 0x03;
	printf_s("0x%X + 0x%x = 0x%X\n", a, b, GFadd(a, b));
	printf_s("0x%X * 0x%X = 0x%X\n", a, b, GFmul(a, b));
	printf_s("0x%X * y = 1, solution: y = 0x%X\n", b, GFinv(b));
	printf_s("0x%X * y = 1, solution: y = 0x%X\n", b, inv(b));
	printf_s("0x%X^y = 0x%X, solution: y = 0x%X\n", g, x, Discrelog(g,x));
	Dispbox();
	system("pause");
	return 0;
}

/*	//v1.0
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
		// bi' = bi ^ b(i+4) ^ b(i+5) ^ b(i+6) ^ b(i+7) ^ {63}
		sbox[i] = btmp^_rotl8(btmp, 4) ^ _rotl8(btmp, 3) ^ _rotl8(btmp, 2) ^ _rotl8(btmp, 1) ^ 0x63;	
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
		cout << "input x, y (all hex): ";
		cin >> hex >> x >> hex >> y;
		cout << "x + y = " << hex << gfadd(x, y) << endl;

		cout << "input x, y (all hex): ";
		cin >> hex >> x >> hex >> y;
		cout << "x * y = " << hex << gfmul(x, y) << endl;

		cout << "input x(hex): ";
		cin >> hex >> x;
		cout << "x * y = 1  solution: y = " << hex << inver(x, inv) << endl;

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
*/