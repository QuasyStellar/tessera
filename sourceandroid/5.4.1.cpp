#include <iostream>
#include <cmath>

using namespace std;

int main() {
    setlocale(LC_ALL, "");
    double x;
    double e = 1e-6;
    double totalSum = 0;
    double term = 1;
    double k = 0;
    cout << "Введите x: ";
    cin >> x;

    if (x < 0) {
        cout << "Факториал отрицательного числа";
    } else {
        while (abs(term) > e) {
            long long f = 1;

            for (int i = 1; i <= (x + k); i++) {
                f *= i;
            }

            term = f / (pow(3, k) * (3 * k + 2));
            totalSum += term;
            k++;
        }

        cout << "Приближенная сумма: " << totalSum << endl;
    }
}
