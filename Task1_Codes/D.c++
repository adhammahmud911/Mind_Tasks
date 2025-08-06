#include <iostream>
#include <vector>
#include <cmath> // for abs()
using namespace std;

// Function to calculate the absolute difference between the sums of diagonals
int diagonalDifference(const vector<vector<int>>& arr) {
    int n = arr.size();
    int primarySum = 0, secondarySum = 0;

    for (int i = 0; i < n; ++i) {
        primarySum += arr[i][i];               // Primary diagonal: arr[0][0], arr[1][1], ...
        secondarySum += arr[i][n - 1 - i];     // Secondary diagonal: arr[0][n-1], arr[1][n-2], ...
    }

    return abs(primarySum - secondarySum);
}

int main() {
    int n;

    // Ask user to input the size of the square matrix
    cout << "Enter the size of the square matrix: ";
    cin >> n;

    vector<vector<int>> arr(n, vector<int>(n));

    // Input matrix elements
    cout << "Enter the matrix elements (" << n * n << " values):" << endl;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> arr[i][j];

    // Calculate and print the diagonal difference
    int result = diagonalDifference(arr);
    cout << "Absolute diagonal difference: " << result << endl;

    return 0;
}
