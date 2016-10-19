#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>


// Still need to work on this. Just empty right now.

const float c = 299792458;

float cToMeter(float x){

  return x * c;

}

float meterToC(float x) {

  return x / c;

}

int main(int argc, char *argv[]) {

  std::cout << cToMeter(0.5) << std::endl;
  return 0;
}
