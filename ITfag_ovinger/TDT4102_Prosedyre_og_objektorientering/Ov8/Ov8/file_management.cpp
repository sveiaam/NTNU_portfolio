#include "file_management.h"
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <algorithm>
#include <map>
#include <sstream>


void writeToFile() {
	bool quit = false;
	std::string s;
	std::ofstream out; //Declaring stream
	out.open("oppg1.txt");
	//out.open("C:\Users\Bruker\Documents\TDT4102\ov8_distant_files\oppg1_extra.txt");

	if (out.fail()) {
		std::cout << "func. writeToFile() failed to open the requested file" << std::endl;
	};

	while (not quit) {
		std::cout << "Write to document:\n";
		std::cin >> s;
		if (s == "quit") {
			quit = true;
		}
		else {
			out << s << "\n";
			std::cout << "\n";
		};
	};
	out.close();
}

void readFromFile(std::string inputFile, std::string outputFile) {
	std::ifstream in; //Declaring in stream
	std::ofstream out; //Declaring out stream
	in.open(inputFile);
	out.open(outputFile);
	if (in.fail()) {
		std::cout << "func. readFromFile() failed to open the input file" << std::endl;
		exit(1);
	};
	if (out.fail()) {
		std::cout << "func. readFromFila() failed to open the output file" << std::endl;
		exit(1);
	};

	int iter = 1;
	std::string s;
	while (std::getline(in, s)) {
		out << iter << " || " << s << "\n";
		iter += 1;
		std::cout << iter << std::endl;
	};

	in.close();
	out.close();
}

void printArray(int arr[], int lenght) {
	char c = 'a';  // Makes table element no i have the i-th letter of the alphabet in front of it
	int counter = 0;  // Begins a new line for every four elements
	for (int i = 0; i < lenght; i++) {
		std::cout.width(5); std::cout << c << ": " << arr[i];
		c += 1;
		counter += 1;
		if (counter % 4 == 0) {
			std::cout << "\n\n";
		};
	};
	std::cout << "\n\n";
}

void characterStatistics(std::string filename) {
	// Make an array of all characters in english
	int table[26] = { 0 };
	std::ifstream in;  // Declare in stream
	in.open(filename);
	if (in.fail()) {
		std::cout << "func. characterStatistics() failed to open the input file" << std::endl;
		exit(1);
	};

	char c;
	int total = -1;  // Initialize to -1 to not count the empty last element of the iteration
	// Iterate over all non-empty char elements in the file and adds one to the correct char place in the table
	while (in.get(c)) {
		table[tolower(c) - 'a'] += 1;
		total += 1;
	};
	in.close();
	// Print the array
	printArray(table, 26);
	std::cout << "Total amount of characters: " << total << std::endl;
}



// Reduce upper-case letters and remove characters not in the english alphabet
std::string reduceWord(std::string word) {
	// The desired characters
	char acceptedLetters[26] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };

	// Pointer to end of the array above
	char *end = acceptedLetters + sizeof(acceptedLetters) / sizeof(acceptedLetters[0]);

	int len = word.length();
	std::string newWord;

	// Check each char in input word if they match with the accepted characters
	for (int i = 0; i < len; i++) {
		// Make a pointer to the first element in acceptedLetters that matches with the char in position i of original word
		//	if it exists. Else make a pointer to the end of the array.
		char *position = std::find(acceptedLetters, end, tolower(word[i]));
		
		// If uppercase letter is found, and it's lowercase is in the list of accepted characters
		if (position != end and isupper(word[i])) {
			newWord.push_back(tolower(word[i]));
		}
		// If symbol is found in the list of accepted characters
		else if (position != end) {
			newWord.push_back(word[i]);
		};
	};
	// The accepted letters have been placed in order of appearance in newWord
	return newWord;
}

// Find amount of each word in a read file
std::map<std::string, int> wordCount(std::string filename) {
	std::ifstream in; // Declaring in stream from file
	in.open(filename);
	if (in.fail()) {
		std::cout << "func. wordCount failed to open the input file" << std::endl;
		exit(1);
	};

	std::map<std::string, int> count;
	std::string line;
	std::string word;
	int lineNo = 0;

	while (std::getline(in, line)) {
		// Get a hold of a single word in the 
		std::stringstream ss(line);
		while (ss >> word) {
			// Not found in map
			if (count.find(word) == count.end()) {
				count.insert({ reduceWord(word), 1 });
			}
			// Found in map
			else {
				count[reduceWord(word)] += 1;
			};
		};
		lineNo += 1;
	};
	in.close();

	// Searching for ### in map yields number of lines*
	count.insert({ "###", lineNo });
	// Remove a "empty" key that is added on the final line
	count.erase("");

	return count;
}

// Sum up all int in given map type
int addMap(std::map<std::string, int> inputMap) {
	int sum = 0;
	for (auto i = inputMap.begin(); i != inputMap.end(); i++) {
		sum += i->second;
	};
	return sum;
}

// Return the string of the longest key in wordcount
std::string longestKey(std::map<std::string, int> intputMap) {
	int longest = 0;
	std::string longestWord;

	for (auto i = intputMap.begin(); i != intputMap.end(); i++) {
		if (i->first.length() > longest) {
			longest = i->first.length();
			longestWord = i->first;
		};
	};
	return longestWord;
}

// Print out the map of wordcount (of given type)
void printWordCount(std::map<std::string, int> wordCount) {
	for (auto i = wordCount.begin(); i != wordCount.end(); i++) {
		std::cout << i->first << ": " << i->second << std::endl;
	};
}

std::string mostCommonKey(std::map<std::string, int> wordCount) {
	int max = 0;
	std::string currentWord;
	for (auto i = wordCount.begin(); i != wordCount.end(); i++) {
		if (i->second > max) {
			max = i->second;
			currentWord = i->first;
		};
	};
	return currentWord;
}

// Answers question 4
void wordStatistics(std::string filename) {
	std::map<std::string, int> wordMap = wordCount(filename);

	// No of lines defined previously to be given by key "###"
	int noOfLines = wordMap["###"];
	// Remove the line number for the rest of the program
	wordMap.erase("###");
	int noOfUniqueWords = wordMap.size();
	int noOfWords = addMap(wordMap);
	std::string longestWord = longestKey(wordMap);
	int lenghtOfLongestWord = longestWord.length();
	std::string mostCommonWord = mostCommonKey(wordMap);
	int occuranceOfMostCommonWord = wordMap[mostCommonWord];

	std::cout << "\nFILE: " << filename << "\n\n\n";
	std::cout << "Number of total words: " << noOfWords << std::endl;
	std::cout << "Number of unique words: " << noOfUniqueWords << std::endl;
	std::cout << "Number of lines: " << noOfLines << std::endl;
	std::cout << "Longest word: '" << longestWord << "' with " << lenghtOfLongestWord << " letters" << std::endl;
	std::cout << "Most common word: '" << mostCommonWord << "' with " << occuranceOfMostCommonWord << " occurrances" << std::endl;
	std::cout << "\nAmount of each word:\n" << std::endl;
	printWordCount(wordMap);
}

