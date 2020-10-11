#include<iostream>
#include<cmath>
#include"bitmap_image.hpp" // стороняя библиотека, использующаяся для работы с изображениями
using namespace std;

int main()
{
	int pixels[128][128]; // структура для хранения значений пикселей
	bitmap_image img("10p1.bmp");

    for (int i = 0; i < 128; i++)
    {
        for (int j = 0; j < 128; j++)
        {
            rgb_t color;
            img.get_pixel(i, j, color.blue, color.red, color.green); // считывание значения пикселей
            pixels[i][j] = color.red;
        }
    }

    for (int i = 0; i < 128; i++) // вывод последовательности
        cout << pixels[i][63] << ' ';                           
    cout << endl;

    int v[14] = { 0 };
    for (int i = 0; i < 128; i++)
    {
        pixels[i][63] = round(pixels[i][63] / 20.0) * 20; //квантование
        v[pixels[i][63] / 20]++; //подсчет частоты встречаемости уникальных символов
        cout << pixels[i][63] << ' '; //вывод последовательности после квантования
    }
    cout << endl;

    for (int i = 0; i < 14; i++) // вывод количества для каждого уникального символа
        cout << i * 20 << ":" << v[i] << "\t";
   
    double ent = 0; //нахождение энтропии
    for (int i = 0; i < 14; i++)
        ent = ent + (v[i] / 128.0) * log2((v[i] / 128.0));
    cout << -ent;

	return 0;

}