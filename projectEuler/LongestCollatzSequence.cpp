/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <iostream>
using namespace std;

int main(){
	int max_length = 0;
	int the_number = 1000000;
	for(int num = the_number; num > 1; num--){
		int chain_length = 0;
		unsigned long int n = num;
		while (n != 1){
			chain_length++;
			if (n%2==0)
				n = n/2;
			else
				n = 3*n+1;
		}
			if (chain_length+1 > max_length){
			max_length = chain_length+1;
			the_number = num;
		}
		//cout << "\nNumber " << num << " has " << chain_length+1 << " length";
	}
	cout << "\nLargest chain length: " << max_length << " by: " << the_number;
	return the_number;
}
