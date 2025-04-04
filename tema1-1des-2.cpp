#include <iostream>
#include <string>

using namespace std;

int main(){
    int largo, ancho, area;
    string texto1="El valor del area es: ",texto2= " y los valores de ancho y largo son: ";
    string explicacion="Este programa solicita el largo y ancho para calcular el área de un rectángulo y mostrarla" ;
    cout << "Ingrese el largo" <<endl;
    cin >> largo;
    cout << "Ingrese el ancho" << endl;
    cin >> ancho;
    area = largo * ancho;
    cout << explicacion << endl;
    cout << texto1 << area << texto2 << largo << " y " <<ancho << endl;
    return 0;
}