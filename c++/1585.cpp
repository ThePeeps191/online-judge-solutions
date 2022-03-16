#include <iostream>
#include <string>
using namespace std;
int main()
{
	int T;
	cin >> T;
	while (T--)
	{
		string test;
		cin >> test;
		int count = 0;
		int previous = 0;
		
		for (int i = 0; i < test.size(); ++i)
		{
			if (test[i] == 'O')
			{
				++previous;
				count += previous;
			}
			else
				previous = 0;
		}
		
		cout << count << '\n';
	}
}