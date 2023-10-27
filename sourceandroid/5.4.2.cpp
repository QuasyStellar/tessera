#include <iostream>

using namespace std;

int main() {
    setlocale(LC_ALL, "");
    int x;
    cout << "Введите натуральное число x: ";
    cin >> x;

    int result = 0;
    int multiplier = 1;

    while (x > 0) {
        int digit = x % 10;
        x /= 10;

        if (digit != 0 && digit != 5) {
            result += digit * multiplier;
            multiplier *= 10;
            cout << result << endl;
        }
    }
    cout << "Результат: " << result << endl;
}
