#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    setlocale(LC_ALL, "");
    int country, g, s, b;
    string name;
    ofstream fout;
    ifstream fin;
    cout << "Введитие кол-во стран: ";
    cin >> country;
    cout << "Введите страну, и кол-во медалей в формате 'Страна Золото Серебро Бронза': " << endl;
    cin.get();
    fout.open("textinput.txt");
    if (fout.is_open()) {
        fout << "Страна" << "\t|" << "Золото" << "\t|" << "Cеребро" << "|" << "Бронза" << "\t|" << "Сумма" << "\t|" << "Сумма очков" << "\n";
        for (int i = 1; i <= country; i++) {
            cin >> name >> g >> s >> b;
            fout << name << "\t|" << g << "\t|" << s << "\t|" << b << "\t|" << g + s + b << "\t|" << 7 * g + 6 * s + 5 * b << "\n";
        }
    }
    else {
        cout << "Произошла ошибка";
    }
    fout.close();
    fin.open("textinput.txt");
    cout << "Итоги зимней Олимпиады в Нагано, 1998 г." << endl;
    if (fin.is_open()) {
        while (getline(fin, name)) {
            cout << name << endl;
        }
    }
    else {
        cout << "Произошла ошибка";
    }
}
