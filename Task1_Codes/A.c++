#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    int n;

    // Ask the user to input the number of elements
    cout << "Enter the number of percentages: ";
    cin >> n;

    vector<int> p(n);
    double sum = 0.0;

    // Ask the user to input each percentage
    cout << "Enter the percentages:\n";
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        sum = sum + p[i];
    }

    // Calculate the average percentage
    double result = sum / n;

    // Display the result with 8 digits after the decimal point
    cout << "Average percentage: " << fixed << setprecision(8) << result << endl;

    return 0;
}
