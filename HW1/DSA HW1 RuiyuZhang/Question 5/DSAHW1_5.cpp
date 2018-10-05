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
double _3sum(vector<int>);
double _2sum(vector<int>);
//NOTICE ABOVE

//main function only is I/O, here I'm only outputting _3sum
int main()
{
	vector<int> data8, data32, data128, data512, data1024, data4096, data4192, data8192;
	ifstream load;
	int loader;
	cout << "[!]Result is in millisecond." << endl;
	cout << left << setw(12) << "SIZE" << left << setw(12) << "TIME" << endl;
	//now 8 int
	load.open("8int.txt", std::fstream::in);
	while (load >> loader) { data8.push_back(loader); }
	cout << left << setw(12) << "8" << setw(12) << _3sum(data8) << endl;
	load.close();
	//now 32 int
	load.open("32int.txt", std::fstream::in);
	while (load >> loader) { data32.push_back(loader); }
	cout << left << setw(12) << "32" << setw(12) << _3sum(data32) << endl;
	load.close();
	//now 128 int
	load.open("128int.txt", std::fstream::in);
	while (load >> loader) { data128.push_back(loader); }
	cout << left << setw(12) << "128" << setw(12) << _3sum(data128) << endl;
	load.close();
	//now 512 int
	load.open("512int.txt", std::fstream::in);
	while (load >> loader) { data512.push_back(loader); }
	cout << left << setw(12) << "512" << setw(12) <<  _3sum(data512) << endl;
	load.close();
	//now 1024 int
	load.open("1024int.txt", std::fstream::in);
	while (load >> loader) { data1024.push_back(loader); }
	cout << left << setw(12) << "1024" << setw(12) <<_3sum(data1024) << endl;
	load.close();
	//now 4096 int
	load.open("4096int.txt", std::fstream::in);
	while (load >> loader) { data4096.push_back(loader); }
	cout << left << setw(12) << "4096" << setw(12) << _3sum(data4096) << endl;
	load.close();
	//now 8192 int
	load.open("8192int.txt", std::fstream::in);
	while (load >> loader) { data8192.push_back(loader); }
	cout << left << setw(12) << "8192" << setw(12) << _3sum(data8192) << endl;
	load.close();

	system("pause");

	return 0;
}

double _3sum(vector<int>data)
{
	time_t nstart, nend;
	int low, high, temp, pair_counter = 0, value1;
	//sort
	sort(data.begin(), data.end());
	//get time
	nstart = clock();
    //real calculation
	for (int array_lookup = 0; array_lookup < data.size(); array_lookup++)
	{
		//let's say sorted array goes from low to high (lowest on the left)
		low = array_lookup+1, high = data.size() - 1;
		while (low < high)
		{
			value1 = data[array_lookup];//define one value, find two other
			temp = data[low] + data[high];
			if (temp == -value1)
			{
				pair_counter++;
				high--;
			}
			else if (temp > -value1)//sum too big, decrese higher side
				high--;
			else //sum too small, increase on lower side
				low++;
		}
		//end of calculation
	}
	nend = clock();
	return double(nend - nstart) *1000 / CLOCKS_PER_SEC;
}

double _2sum(vector<int>data)
{
	time_t nstart, nend;
	int low, high, temp, pair_counter = 0;
	low =0, high = data.size() - 1;
	//sort
	sort(data.begin(), data.end());
	//get time
	nstart = clock();
    //real calculation
	while (low < high)
	{
		temp = data[low] + data[high];
		if (temp == 0)
		{
			cout << "\n" << data[low] << "+" << data[high] << "=0";
			pair_counter++;
			high--;
		}
		else if (temp > 0)//sum too big, decrese higher side
			high--;
		else //sum too small, increase on lower side
			low++;
	}
		//end of calculation
	nend = clock();
	return double(nend - nstart) * 1000 / CLOCKS_PER_SEC;
}