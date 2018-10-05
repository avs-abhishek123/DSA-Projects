// RUIYU ZHANG rz213
// DSA HW1 Q1

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>  
#include <ctime>
#include <iomanip>
#include <vector>
using namespace std;
//NOTICE BELOW
//algorthms are in these two funtions below
double naive(vector<int>);
double complex(vector<int>);
//NOTICE ABOVE

int main()
{
	vector<int> data8,data32,data128,data512,data1024, data4096,data4192,data8192;
	ifstream load;
	int loader;
	
	//below are I/O
	cout << "[!]Result is 5-time-average, in millisecond." << endl;
	cout <<   setw(8)<< "SIZE" <<   setw(12) <<  "NAIVE"<<   setw(12)<<"   COMPLEX" << endl;
	//now 8 int
	load.open("8int.txt", std::fstream::in);
	while (load >> loader) { data8.push_back(loader); }
	cout <<   setw(8) << "8" <<   setw(12) << naive(data8) <<  setw(12) << complex(data8) << endl;
	load.close();
	//now 32 int
	load.open("32int.txt", std::fstream::in);
	while (load >> loader) { data32.push_back(loader); }
	cout <<   setw(8) << "32" <<   setw(12) <<  naive(data32) <<   setw(12) << complex(data32) << endl;
	load.close();
	//now 128 int
	load.open("128int.txt", std::fstream::in);
	while (load >> loader) { data128.push_back(loader); }
	cout <<   setw(8) << "128" <<   setw(12) <<  naive(data128) <<   setw(12) << complex(data128) << endl;
	load.close();
	//now 512 int
	load.open("512int.txt", std::fstream::in);
	while (load >> loader) { data512.push_back(loader); }
	cout <<   setw(8) << "512" <<   setw(12) <<  naive(data512) <<   setw(12) << complex(data512) << endl;
	load.close();
	//now 1024 int
	load.open("1024int.txt", std::fstream::in);
	while (load >> loader) { data1024.push_back(loader); }
	cout <<   setw(8) << "1024" <<   setw(12) <<  naive(data1024) <<   setw(12) << complex(data1024) << endl;
	load.close();
	//now 4096 int
	load.open("4096int.txt", std::fstream::in);
	while (load >> loader) { data4096.push_back(loader); }
	cout <<   setw(8) << "4096" <<   setw(12) <<  naive(data4096) <<   setw(12) << complex(data4096) << endl;
	load.close();
	//now 4192 int
	load.open("4192int.txt", std::fstream::in);
	while (load >> loader) { data4192.push_back(loader); }
	cout <<   setw(8) << "4192" <<   setw(12) <<  naive(data4192) <<   setw(12) << complex(data4192) << endl;
	load.close();
	//now 8192 int
	load.open("8192int.txt", std::fstream::in);
	while (load >> loader) { data8192.push_back(loader); }
	cout <<   setw(8) << "8192" <<   setw(12) <<  naive(data8192) <<   setw(12) << complex(data8192) << endl;
	load.close();
	system("pause");
    return 0;
}


double naive(vector<int> ndata)
{
	time_t nstart,nend,TOTAL=0;
	for (int average_counter=0; average_counter<5; average_counter++)
	{ 
		//now calc naive
		int ncount = 0, n1, n2, n3, n;
		n = ndata.size();
		nstart = clock();
		for (n1 = 0; n1 < n; n1++)
			for (n2 = n1 + 1; n2 < n; n2++)
				for (n3 = n2 + 1; n3 < n; n3++)
					if (n1 + n2 + n3 == 0)ncount++;
		nend = clock();
		TOTAL += (nend - nstart);
	}
	return double(TOTAL) / 5*1000 / CLOCKS_PER_SEC;//shown in ms
}

double complex(vector<int> cdata)
{
	time_t cstart,cend, TOTAL2=0;
	for (int average_counter2 = 0; average_counter2<5; average_counter2++)
	{ 
		//now calc complx
		int ccount = 0, c1, c2, x, c, low, high, mid;
		c = cdata.size();
		cstart = clock();
		//now sort
		sort(cdata.begin(), cdata.end());
		//now find
		for (c1 = 0; c1 < c; c1++)
		{
			for (c2 = c1 + 1; c2<c; c2++)
			{
				x = 0 - c1 - c2;//what we are looking for
				low = c2 + 1;
				high = c - 1;
				while (low <= high)
				{
					mid = (low + high) / 2;
					if (cdata[mid] == x) { ccount++; }//found
					else if (x<cdata[mid]) { high = mid - 1; }//go left
					else { low = mid + 1; }//go right
				}
			}
		}
		cend = clock();
		TOTAL2 += (cend - cstart);
	}
	return double(TOTAL2) / 5 * 1000 / CLOCKS_PER_SEC;//runned 5 times, average is returned
}
