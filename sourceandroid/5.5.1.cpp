#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    setlocale(LC_ALL, "");
    ofstream fout, frs;
    ifstream fin;
    int m, n;
    cout << "Введите размеры матриц 'm n': ";
    cin >> m >> n;
    fout.open("matrix.txt");
    frs.open("result.txt");
    if (fout.is_open() and frs.is_open()){
        frs << "Матрица\t| 0\t| 1\t| 2\t| 3\t| 4\t| 5\t| 6\t| 7\t| 8\t| 9\t|\n";
        string** zapis = new string* [m*n];
        for (int i = 0; i < m*n; ++i) {
            zapis[i] = new string[10];
        }
        for (int i = 0; i < m*n; ++i) {
            for (int j = 0; j < 10; ++j) {
                zapis[i][j] = "-";
            }
        }
        for (int numm = 1; numm <= 10; numm++) {
            int** matr = new int* [m];
            for (int i = 0; i < m; ++i) {
                matr[i] = new int[n];
            }

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    int num = rand() % 10;
                    int k = 0;
                    while (zapis[k][num] != "-") {
                        k += 1;
                    }
                    zapis[k][num] = to_string(i+1) + "x" + to_string(j+1);
                    matr[i][j] = num;
                }
            }
            frs << "Матрица" << numm<<"|";
            for (int i = 0; i < m*n; ++i) {
                for (int j = 0; j < 10; ++j) {
                    frs << zapis[i][j] << "\t|";
                }
                frs << endl << "\t|";

            }
            frs << endl;
            fout << endl;
            fout << "Матрица №" << numm << " " << m << " x " << n << endl;
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    fout << matr[i][j] << ", ";
                }
                fout << endl;
            }
            fout << endl;
        }
        fout.close();
        frs.close();

    }
        
    else {
        cout << "Произошла ошибка";
    }
}
