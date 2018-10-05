// RUIYU ZHANG rz213
// DSA HW1 Q5


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
double farpair(vector<int>);
//NOTICE ABOVE

//main function only is I/O, here I'm only outputting farpair
int main()
{
	vector<int> data8, data32, data128, data512, data1024, data4096, data4192, data8192;
	ifstream load;
	int loader;
	cout << "[!]Result is 100-run-average, in microsecond." << endl;
	cout << left << setw(12) << "SIZE" << left << setw(12) << "TIME" << endl;
	//now 8 int
	load.open("8int.txt", std::fstream::in);
	while (load >> loader) { data8.push_back(loader); }
	cout << left << setw(12) << "8" << setw(12)  << farpair(data8) << endl;
	load.close();
	//now 32 int
	load.open("32int.txt", std::fstream::in);
	while (load >> loader) { data32.push_back(loader); }
	cout << left << setw(12) << "32" << setw(12)  << farpair(data32) << endl;
	load.close();
	//now 128 int
	load.open("128int.txt", std::fstream::in);
	while (load >> loader) { data128.push_back(loader); }
	cout << left << setw(12) << "128" << setw(12)  << farpair(data128) << endl;
	load.close();
	//now 512 int
	load.open("512int.txt", std::fstream::in);
	while (load >> loader) { data512.push_back(loader); }
	cout << left << setw(12) << "512" << setw(12)  << farpair(data512) << endl;
	load.close();
	//now 1024 int
	load.open("1024int.txt", std::fstream::in);
	while (load >> loader) { data1024.push_back(loader); }
	cout << left << setw(12) << "1024" << setw(12)  << farpair(data1024) << endl;
	load.close();
	//now 4096 int
	load.open("4096int.txt", std::fstream::in);
	while (load >> loader) { data4096.push_back(loader); }
	cout << left << setw(12) << "4096" << setw(12) <<  farpair(data4096) << endl;
	load.close();
	//now 8192 int
	load.open("8192int.txt", std::fstream::in);
	while (load >> loader) { data8192.push_back(loader); }
	cout << left << setw(12) << "8192" << setw(12) <<  farpair(data8192) << endl;
	load.close();

	system("pause");

	return 0;
}

double farpair(vector<int>data)
{
	time_t nstart,nend;
	int big = data[0], smll = data[0],temp;
	//get time
	nstart = clock();
	//real calculation
	for (int runtime=1;runtime<=100;runtime++)//loop for 100 times, get average
	{ 
		for (int search = 0; search < data.size(); search++)
		{
			temp = data[search];
			if (temp > big)big = temp;
			else if (temp < smll)smll = temp;
			else {}
		}
	}
	//end of calculation
	nend = clock();
        return double(nend-nstart)*10000/CLOCKS_PER_SEC;
}
