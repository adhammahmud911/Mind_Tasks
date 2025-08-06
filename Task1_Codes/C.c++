#include <iostream>
using namespace std;

int main() {
    int t;

    // Ask for the number of test cases
    cout << "Enter the number of test cases: ";
    cin >> t;
    
    while (t--) {
        int n;

        // Ask for the number to divide
        cout << "Enter a number: ";
        cin >> n;

        // Output the result of integer division by 2
        cout << "Result (n / 2): " << n / 2 << endl;
    }

    return 0;
}
