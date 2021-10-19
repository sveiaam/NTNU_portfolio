#pragma once

//1
int incrementByValueNumTimes(int startValue, int increment, int numTimes);
void incrementByValuesNumTimes2(int *startValue, int increment, int numTimes);
void swapNumbers(int *a, int *b);

//2
void printArray(int table[], int n);
int randomWithLimits(int maxLim, int minLim);
void randomizeArray(int table[], int n);

//3
void sortArray(int table[], int n);
double medianOfArray(int sortedTable[], int n);

//4
void randomizeCString(char table[], int n, char lowerLim, char upperLim);
void readInputToCString(char table[], int n, char lowerLim, char upperLim);
int countOccurencesOfCharacter(char table[], int n, char target);
void fillOccurenceTable(int occurences[], char table[], int lenOcc, int lenTable, char firstValue);
double gradeAverage(int table[], int n);
