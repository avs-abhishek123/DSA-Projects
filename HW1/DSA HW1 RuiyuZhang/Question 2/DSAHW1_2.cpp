//RUIYU ZHANG rz213
//DSA HW2 Q2

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>  
#include <ctime>
#include <iomanip>
#include <vector>
using namespace std;

double qfind(vector<int>, vector<int>);
double qunion(vector<int>, vector<int>);
double w_qunion(vector<int>, vector<int>);
int root(int, vector<int>);

int main()
{
	vector<int> data8, data32, data128, data512, data1024, data4096, data8192,id(8192);
	ifstream load;
	int loader, id_cleaner;
	for (id_cleaner = 0; id_cleaner < 8192; id_cleaner++)
		id[id_cleaner] = id_cleaner;//reset, initialize
	cout << "[!]Result is in millisecond." << endl;
	cout << left << setw(8) << "SIZE" << left << setw(15) << "Q-Find" << left << setw(15) << "Q-Union"<< left << setw(15) << "WQ-Union" << endl;
	//now 8 pair
	load.open("8pair.txt", std::fstream::in);
	while (load >> loader) { data8.push_back(loader); }
	cout << left << setw(8) << "8" << setw(12) << qfind(data8,id) <<"  "<< setw(12) <<qunion(data8,id) << "  " << setw(12) <<w_qunion(data8, id) << endl;
	load.close();
	//now 32 pair
	load.open("32pair.txt", std::fstream::in);
	while (load >> loader) { data32.push_back(loader); }
	cout << left << setw(8) << "32" << setw(12) << qfind(data32, id) << "  " << setw(12) <<qunion(data32, id) << "  " <<setw(12) <<w_qunion(data32, id) << endl;
	load.close();
	//now 128 pair
	load.open("128pair.txt", std::fstream::in);
	while (load >> loader) { data128.push_back(loader); }
	cout << left << setw(8) << "128" << setw(12) << qfind(data128, id) << "  " << setw(12) <<qunion(data128, id) << "  " << setw(12) <<w_qunion(data32, id) << endl;
	load.close();
	//now 512 pair
	load.open("512pair.txt", std::fstream::in);
	while (load >> loader) { data512.push_back(loader); }
	cout << left << setw(8) << "512" << setw(12) << qfind(data512, id) << "  " << setw(12) <<qunion(data512, id) << "  " << setw(12) <<w_qunion(data512, id) << endl;
	load.close();
	//now 1024 pair
	load.open("1024pair.txt", std::fstream::in);
	while (load >> loader) { data1024.push_back(loader); }
	cout << left << setw(8) << "1024" << setw(12) << qfind(data1024, id) << "  " << setw(12) <<qunion(data1024, id) << "  " << setw(12) <<w_qunion(data1024, id) << endl;
	load.close();
	//now 4096 pair
	load.open("4096pair.txt", std::fstream::in);
	while (load >> loader) { data4096.push_back(loader); }
	cout << left << setw(8) << "4096" << setw(12) << qfind(data4096, id) << "  " << setw(12) << qunion(data4096, id) << "  " << setw(12) << w_qunion(data4096, id) << endl;
	load.close();
	//now 8192 pair
	load.open("8192pair.txt", std::fstream::in);
	while (load >> loader) { data8192.push_back(loader); }
	cout << left << setw(8) << "8192" << setw(12) << qfind(data8192, id) << "  " << setw(12) << qunion(data8192, id) << "  " << setw(12) << w_qunion(data8192, id) << endl;
	load.close();


	
	system("pause");
        return 0;
}


double qfind(vector<int> data1, vector<int> id1)
{
	int p1, p2,p3, p2_original;
	time_t fstart,fend;
        fstart = clock();
	for (int i1 = 0; i1 < data1.size(); i1 += 2)
	{
		p1 = data1[i1], p2 = data1[i1 + 1];
		//make sure p1>=p2
		if (p1 < p2)
		{
			p3 = p1;
			p1 = p2;
			p2 = p3;
		}
		else{}
		//set tag to p1
		p2_original = p2;
		for (int p2_set = 0; p2_set < 8192; p2_set++)
		{
			if (id1[p2_set] == p2_original)
				id1[p2_set] = p1;
		}
	}
	fend = clock();
	return double(fend-fstart) * 1000/ CLOCKS_PER_SEC;//parameter: ms
}
double qunion(vector<int> data2, vector<int> id2)
{
	int u1, u2;
	time_t ustart,uend;
        ustart = clock();
	for (int i2 = 0; i2 < data2.size(); i2 += 2)
	{
		u1 = data2[i2], u2 = data2[i2 + 1];
		if (root(u1, id2) != root(u2, id2))
			id2[root(u1, id2)] = root(u2, id2);//change root: u1's root->u2's root
		else {};
	}
	uend = clock();
	return double(uend-ustart) * 1000/ CLOCKS_PER_SEC;//parameter: ms
}
double w_qunion(vector<int> data3, vector<int> id3)
{
	int w1, w2,w3,w4;
	vector<int> sz(8192, 1);
	time_t wstart,wend;
        wstart = clock();
	for (int i2 = 0; i2 < data3.size(); i2 += 2)
	{
		w1 = data3[i2], w2 = data3[i2 + 1];
		w3 = root(w1, id3), w4 = root(w2, id3);
		if (w3 != w4)
		{
			if (sz[w3] < sz[w4])
			{
				id3[w3] = w4; //change root: w1->w2
				sz[w4] += sz[w3];
			}
			else
			{
				id3[w4] = w3;//change root: w2->w1
				sz[w3] += sz[w4];
			}
		}
		else{}
	}
	wend = clock();
	return double(wend-wstart) * 1000/ CLOCKS_PER_SEC;//parameter: ms
}

int root(int r, vector<int>idr)
{
	while (r != idr[r])
		r = idr[r];
	return r;
}


