#include<iostream>
#include<cmath>
#include"bitmap_image.hpp"
using namespace std;

int main()
{
	int pixels[128][128];
	bitmap_image img("10p1.bmp");

    for (int i = 0; i < 128; i++)
    {
        for (int j = 0; j < 128; j++)
        {
            rgb_t color;
            img.get_pixel(i, j, color.blue, color.red, color.green);
            pixels[i][j] = color.red;
        }
    }

    for (int i = 0; i < 128; i++)
        cout << pixels[i][63] << ' ';                           
    cout << endl;

    int v[14] = { 0 };
    for (int i = 0; i < 128; i++)
    {
        pixels[i][63] = round(pixels[i][63] / 20.0) * 20;
        v[pixels[i][63] / 20]++;
        cout << pixels[i][63] << ' ';
    }
    cout << endl;

    for (int i = 0; i < 14; i++)
        cout << i * 20 << ":" << v[i] << "\t";
   


	return 0;

}