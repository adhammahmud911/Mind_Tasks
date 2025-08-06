#include <iostream>
#include <vector>
using namespace std;

// Function to count apples and oranges that fall on the house
void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
    int appleCount = 0;
    int orangeCount = 0;

    // Check each apple's landing position
    for (int d : apples) {
        int position = a + d;
        if (position >= s && position <= t) {
            appleCount++;
        }
    }

    // Check each orange's landing position
    for (int d : oranges) {
        int position = b + d;
        if (position >= s && position <= t) {
            orangeCount++;
        }
    }

    // Output the counts
    cout << "Apples on the house: " << appleCount << endl;
    cout << "Oranges on the house: " << orangeCount << endl;
}

int main() {
    int s, t;
    cout << "Enter the start and end points of the house (s t): ";
    cin >> s >> t;

    int a, b;
    cout << "Enter the positions of the apple tree and orange tree (a b): ";
    cin >> a >> b;

    int m, n;
    cout << "Enter number of apples and oranges (m n): ";
    cin >> m >> n;

    vector<int> apples(m);
    vector<int> oranges(n);

    cout << "Enter distances at which each apple falls from the apple tree: ";
    for (int i = 0; i < m; i++) {
        cin >> apples[i];
    }

    cout << "Enter distances at which each orange falls from the orange tree: ";
    for (int i = 0; i < n; i++) {
        cin >> oranges[i];
    }

    countApplesAndOranges(s, t, a, b, apples, oranges);

    return 0;
}
