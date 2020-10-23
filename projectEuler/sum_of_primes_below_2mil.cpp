#include <iostream>
#include <time.h>

using namespace std;

long long int primes(){
	long int toCheck = 2;
	long int Divisors[500000];
	Divisors[0] = 2;
	Divisors[1] = 3;
	int length_divisors = 2;
	long long int out = 2+3;
	while (toCheck < 2000000) {
		long int undivided = 0;
		for (int indx = 0; indx < length_divisors; indx++){
			if (toCheck%Divisors[indx] != 0){
				undivided++;
			}
			else
				break;
		}

		if (undivided == length_divisors){
			Divisors[length_divisors] = toCheck;
			length_divisors++;
			out += toCheck;
			//if (toCheck > 900000)
			//	cout << toCheck << " ";
		}
		toCheck++;
	}
	return out;
}

int main(){
	cout << "Process Initiated! \n";
    clock_t tStart = clock();
	cout << "\n\nThe sum of primes is: " << primes();
    printf("\n\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
	return 0;
}
