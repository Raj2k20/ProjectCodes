#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main(int argc, char **argv) {
   cout << "Enter the dimension of the matrices: ";
   int n;
   cin >> n;
   cout << "Enter the 1st matrix: ";
   double matrix1[n][n];
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
         cin >> matrix1[i][j];
      }
   }
   cout << "Enter the 2nd matrix: ";
   double matrix2[n][n];
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
         cin >> matrix2[i][j];
      }
   }
   cout << "Enter the result matrix: ";
   double matrix3[n][n];
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
         cin >> matrix3[i][j];
      }
   }
   double a[n][1];
   for (int i = 0; i < n; i++) {
      a[i][1] = rand() % 2;
   }
   double matrix2a[n][1];
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < 1; j++) {
         for (int k = 0; k < n; k++) {
            matrix2a[i][j] = matrix2a[i][j] + matrix2[i][k] * a[k][j];
         }
      }
   }
   double matrix3a[n][1];
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < 1; j++) { 
         for (int k = 0; k < n; k++) {
            matrix3a[i][j] = matrix3a[i][j] + matrix3[i][k] * a[k][j];
         }
      }
   }
   double matrix12a[n][1];
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < 1; j++) {
         for (int k = 0; k < n; k++) {
            matrix12a[i][j] = matrix12a[i][j] + matrix1[i][k] *matrix2a[k][j];
         }
      }
   }
   for (int i = 0; i < n; i++) {
      matrix12a[i][0] -= matrix3a[i][0];
   }
   bool flag = true;
   for (int i = 0; i < n; i++) {
      if (matrix12a[i][0] == 0)
         continue;
      else
         flag = false;
   } 
   if (flag == true)
      cout << "This is the resultant matrix";
   else
      cout << "This is not the resultant matrix";
}
