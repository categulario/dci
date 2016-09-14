#include <iostream>
#include <fstream>
#include <map>
#include <cstdlib>

using namespace std;

int nComas(string s)
{
	int n = 0;
	for(int i = 0; i < s.length(); i++)
	{
		if(s[i]==',')
		{
			n++;
		}
	}
	return n;
}

float numberSS(string s, int  i, int j)
{
	float x = atof(s.substr( i, j).c_str());
	return x;
}

int main()
{
	ifstream bdcvs;
	string registro;
	map<int, int> semana;
	map<int, int> hora;
	map<int, int> sentido;
	int n, noComasRegistroActual, indexAux, index;
 	bdcvs.open("21201DGST05ZONA15AMOZOC.csv", ios::in);
	if(bdcvs.is_open())
 	{
 		while(!bdcvs.eof())
 		{
 			getline(bdcvs, registro);
 			n = registro.length();
 			noComasRegistroActual = 0;
 			for (int i = 0; i < n; i++)
 			{
 				if(registro[i] == ',')
 				{
 					noComasRegistroActual ++;
 					if(noComasRegistroActual == 3)
 					{
 						indexAux = i;
 					}else if(noComasRegistroActual == 4)
 					{
 						index = i;
 						semana[numberSS(registro, indexAux+1, indexAux)] ++;
 						indexAux = index;
 					}else if(noComasRegistroActual == 5)
 					{
 						index = i;
 						sentido[numberSS(registro, indexAux+1, indexAux)] ++;
 						indexAux = index;
 					}else if(noComasRegistroActual == 6)
 					{
 						index = i;
 						hora[numberSS(registro, indexAux+1, indexAux)] ++;
 					}
 				}

 			}
 		}
 		bdcvs.close();
 	}
 	for (int i = 1; i < 8; i++)
 	{
 		cout << i <<".- " << semana[i] << " | ";
 	}
 	cout << endl;
 	for (int i = 0; i < 3; i++)
 	{
 		cout << i <<".- " << sentido[i] << " | ";
 	}
 	cout << endl;
 	for (int i = 0; i < 24; i++)
 	{
 		cout << i <<".- " << hora[i] << " | ";
 	}
 	cout << endl;
	return 0;
}