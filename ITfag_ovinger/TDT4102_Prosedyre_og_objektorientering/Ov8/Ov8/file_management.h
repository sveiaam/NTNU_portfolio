#pragma once
#include <string>
#include <map>

void writeToFile();
void readFromFile(std::string inputFile, std::string outputFile);
void printArray(int arr[], int lenght);
void characterStatistics(std::string filename);

std::string reduceWord(std::string word);
std::map<std::string, int> wordCount(std::string filename);
int addMap(std::map<std::string, int> inputMap);
std::string longestKey(std::map<std::string, int> intputMap);
void printWordCount(std::map<std::string, int> wordCount);
std::string mostCommonKey(std::map<std::string, int> wordCount);
void wordStatistics(std::string filename);
