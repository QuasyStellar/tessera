#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void openf() {
    ifstream fin;
    string lines, shortestPhrase = "", tempPhrase = "";
    int minPhraseLength = INT_MAX;
    fin.open("textinput.txt");
    if (fin.is_open()) {
        while (getline(fin, lines)) {
            int PhraseLength = 0;
            for (char character : lines) {
                if (isalpha(character) or (character == ' ') or (character == '-') and (character != '.') and (character != ',') and (character != ':') and (character != ';')) {
                    PhraseLength++;
                    if (character == ' ' or character == '-') {
                        PhraseLength--;
                    }
                    if (PhraseLength > 0) {
                        tempPhrase += character;
                    }
                }
                else {
                    if (PhraseLength > 0 && PhraseLength < minPhraseLength) {
                        minPhraseLength = PhraseLength;
                        shortestPhrase = tempPhrase;
                    }
                    PhraseLength = 0;
                    tempPhrase = "";
                }
            }

            if (PhraseLength > 0 && PhraseLength < minPhraseLength) {
                minPhraseLength = PhraseLength;
                shortestPhrase = tempPhrase;
            }
        }

        if (minPhraseLength != INT_MAX) {
            cout << "Самоя короткая фраза: " << shortestPhrase << endl;
            cout << "Длина: " << minPhraseLength << endl;
        }
        else {
            cout << "Файл не содержит фраз." << endl;
        }
    }
    else {
        cout << "Произошла ошибка при открытии файла." << endl;
    }
    fin.close();
}

void createf() {
    string lines, shortestPhrase = "", tempPhrase = "";
    int linesc;
    int minPhraseLength = INT_MAX;
    ofstream fout;
    ifstream fin;
    fout.open("textinput.txt");
    cout << "Введите кол-во строк которые будут записаны: ";
    cin >> linesc;
    cin.get();
    if (fout.is_open()) {
        for (int i = 1; i <= linesc; i++) {
            getline(cin, lines);
            fout << lines << "\n";
        }
    }
    else {
        cout << "Произошла ошибка";
    }
    fout.close();
    fin.open("textinput.txt");
    if (fin.is_open()) {
        while (getline(fin, lines)) {
            int PhraseLength = 0;
            for (char character : lines) {
                if (isalpha(character) or (character == ' ') or (character == '-') and (character != '.') and (character != ',') and (character != ':') and (character != ';')) {
                    PhraseLength++;
                    if (character == ' ' or character == '-') {
                        PhraseLength--;
                    }
                    if (PhraseLength > 0) {
                        tempPhrase += character;
                    }
                }
                else {
                    if (PhraseLength > 0 && PhraseLength < minPhraseLength) {
                        minPhraseLength = PhraseLength;
                        shortestPhrase = tempPhrase;
                    }
                    PhraseLength = 0;
                    tempPhrase = "";
                }
            }

            if (PhraseLength > 0 && PhraseLength < minPhraseLength) {
                minPhraseLength = PhraseLength;
                shortestPhrase = tempPhrase;
            }
        }

        if (minPhraseLength != INT_MAX) {
            cout << "Самоя короткая фраза: " << shortestPhrase << endl;
            cout << "Длина: " << minPhraseLength << endl;
        }
        else {
            cout << "Файл не содержит фраз." << endl;
        }
    }
    else {
        cout << "Произошла ошибка при открытии файла." << endl;
    }
    fin.close();
}

int main() {
    setlocale(LC_ALL, "");
    char ans;
    cout << "Открыть файл или создать? o/c: ";
    cin >> ans;
    switch (ans) {
    case 'o': openf(); break;
    case 'c': createf(); break;
    default: cout << "Неверный ввод";
    }
}
