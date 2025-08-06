#include <iostream>
#include <algorithm> 

using namespace std;

int main() {
    int k2, k3, k5, k6;

    // Input quantities of digits
    cout << "Enter counts of k2, k3, k5, and k6: ";
    cin >> k2 >> k3 >> k5 >> k6;

    // Step 1: Make as many 256s as possible (needs one of each: 2, 5, 6)
    int num256 = min({k2, k5, k6});
    cout << "Number of 256s formed: " << num256 << endl;
    k2 -= num256;  // Use up 2s used in 256s

    // Step 2: Make as many 32s as possible (needs one 2 and one 3)
    int num32 = min(k2, k3);
    cout << "Number of 32s formed: " << num32 << endl;

    // Step 3: Calculate total sum
    int sum = num256 * 256 + num32 * 32;
    cout << "Total sum: " << sum << endl;

    return 0;
}
