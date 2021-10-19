#include <iostream>
#include <iomanip>
#include <cmath>
#include <math.h>
using namespace std;

//Oppg 1

//a)
void inputAndPrintInteger() { //Printer et heltall fra bruker
	int a = 0;
	cout << "Skriv inn et heltall: ";
	cin >> a;
	cout << "\nDu skrev: " << a << "\n" << endl;
}

//b)
int inputInteger() { //Tar inn og returnerer et heltall fra bruker
	int a = 0;
	cout << "Skriv inn et heltall: ";
	cin >> a;
	return a;
}

//c) og d)
void inputIntegersAndPrintSum() { //Printer summen av to tall fra bruker
	int a = inputInteger(), b = inputInteger(); //bruker inputInteger fordi jeg vil ha en returverdi, og dessuten ikke vil printe verdiene underveis.
	cout << "Summen er: " << a + b << endl;
}

//e)
bool isOdd(int n) { //true for n er et oddetall
	return (n % 2) == 1;
}

//f)
void printHumanReadableTime(int sek) { //Printer et antall sekunder i formatet år:døgn:timer:minutter:sekunder
	int sekunder = 0, minutter = 0, timer = 0, dogn = 0, aar = 0;
	aar = sek / 31536000, sek = sek % 31536000;
	dogn = sek / 86400, sek = sek % 86400;
	timer = sek / 3600, sek = sek % 3600;
	minutter = sek / 60, sekunder = sek % 60;
	
	cout << aar << " år, " << dogn << " døgn, " << timer << " timer, " << minutter << " minutter, " << sekunder << " sekunder." << endl;
}

//Oppg 2

//a) og b)
void inputIntegersUsingLoopAndPrintSum() { //Printer ut summen av heltall bruker skriver inn, avsluttes ved 0
	cout << "\nI denne funksjonen skal du skrive inn tall som summeres. Hvis du skriver inn 0 avsluttes prosessen, og summen printes. \n" << endl;
	int adder = 0;
	while (true) {
		int k = inputInteger();
		if (k == 0) {
			break;
		};
		adder += k;
	}
	cout << "Summen av tallene er: " << adder << endl;
	//Hvis bruker først skriver inn antall tall som skal summeres, kan en for-løkke godt brukes (du ville iterert opp til n)
	//Hvis bruker skriver inn 0 for å fullføre summeringen, bør en while-løkke brukes, siden man ikke på forhånd kan oppgi iterasjonsgrensen n
}

//c)
double inputDouble() { //Tar inn og returnerer et flyttall fra bruker
	double a = 0;
	cout << "Skriv inn et tall: ";
	cin >> a;
	return a;
}

//d) og e)
void NOKtoEURO() {
	cout << "Dette programmet konverterer en sum i NOK til en sum i Euro" << endl;
	double NOK = 0;
	while (true) {
		NOK = inputDouble();
		if (NOK >= 0) {
			break;
		};
		cout << "Skriv inn et positivt tall!" << endl;
	};
	cout << NOK << " kroner er " << fixed << showpoint << setprecision(2) << NOK / 9.64 << " Euro." << endl;
	//fixed << showpoint gir 2 desimaler i stedet for 2 gjeldende sifre

	//Bør ikke bruke inputInteger, fordi oppgaven spør om å la brukeren gi beløpet som et positivt desimaltall.
}

//Oppg 3)

//b)
void mult_table() { //tar inn heltallene m og n fra bruker, og printer en m x n gangetabell
	int hoyde = 0, bredde = 0;
	while (true) {
		cout << "Tabellens bredde: ";
		bredde = inputInteger();
		if (bredde > 0) {
			break;
		};
		cout << "Skriv inn et positivt heltall!";
	}
	while (true) {
		cout << "Tabellens høyde: ";
		hoyde = inputInteger();
		if (hoyde > 0) {
			break;
		};
		cout << "Skriv inn et positivt heltall!";
	}
	cout << "\n";
	for (int i = 1; i <= hoyde; i++) {
		for (int j = 1; j <= bredde; j++) {
			cout.width(4); cout << i * j;
		};
		cout << "\n";
	};
	cout << "\n";
	//Funksjonen printer av og til ut \n av estetiske grunner
}

//Oppg 4)

//a)
double discriminant(double a, double b, double c) { //Returnerer diskriminant
	return roundf((b * b - 4 * a * c)*100)/100;
}
															
//b)
void printRealRoots(double a, double b, double c) { //Printer de reelle løsningene av ax^2+bx+c=0
	double d = discriminant(a, b, c);
	if (d > 0) {
		double x1 = (-b + sqrt(discriminant(a, b, c))) / (2 * a), x2 = (-b - sqrt(discriminant(a, b, c))) / (2 * a);
		cout << "Reelle løsninger er: " << fixed << showpoint << setprecision(2) << x1 << " og " << x2 << endl;
	}
	else if (d < 0) {
		cout << "Ingen reelle løsninger." << endl;
	}
	else {
		double x = -b / (2 * a);
		cout << "Reell løsning er: " << fixed << showpoint << setprecision(2) << x << endl;
	}
}

//c), d) og e)
void solveQuadraticEquation() {
	double a = 0, b = 0, c = 0;
	while (true) {
		cout << "Verdien for a: ";
		cin >> a;
		if (a != 0) {
			break;
		};
		cout << "a kan ikke være 0 \n";
	}
	cout << "Verdien for b: ";
	cin >> b;
	cout << "Verdien for c: ";
	cin >> c;
	cout << "\n";
	printRealRoots(a, b, c);
	cout << "\n";
	}

//Oppg 5

//a) og b)
void calculateLoanPayments() { //Printer ut en tabell over innbetalinger og gjenstående beløp for en 10 års (årlig) nedbetalingsplan av et lån
	cout << "Programmet beregner årlige innbetalinger for lån. Spesifiser lånebeløp og rente i prosent" << endl;
	double lanebelop = 0, rente = 0;
	cout << "Lånebeløp: ";
	while (true) {
		lanebelop = inputDouble();
		if (lanebelop > 0) {
			break;
		};
		cout << "Skriv inn et positivt tall!" << endl;
	};
	cout << "Rente (i %): ";
	while (true) {
		rente = inputDouble();
		if (rente >= 0) {
			break;
		};
		cout << "Skriv inn et positivt tall!" << endl;
	};
	int counter = 1;
	double totalbelop = lanebelop, innbetaling = 0;
	cout << "\nÅr\tInnbetaling\tGjenstående lån" << endl;
	while (counter <= 10) {
		innbetaling = totalbelop / 10 + rente / 100 * lanebelop;
		lanebelop = lanebelop - innbetaling + rente/100 * lanebelop;
		cout << counter << "\t" << innbetaling << "\t\t" << lanebelop << endl;
		counter += 1;
	}
	cout << "\n\n";
}

//Oppg 3a
int main() {
	setlocale(LC_ALL, "Norwegian");
	char valg = ' ';
	bool quit = false;
	while (! quit) {
		cout << "::::::::::::::::::::::::::::::::::::::::::::\n\n";
		cout << "Tast en bokstav for å kjøre korresponderende funksjon\n\n";
		cout << "(a) - Sekunder til menneskelig leselig tekst\n";
		cout << "(b) - NOK konvertert til Euro\n";
		cout << "(c) - Gangetabell \n";
		cout << "(d) - Løsning av 2.gradslikning\n";
		cout << "(e) - Beregne innbetaling av lån\n\n";
		cout << "(q) - Avslutt\n\n";
		cin >> valg;
		switch (valg) {
		case 'a':
			printHumanReadableTime(inputInteger());
			break;
		case 'b':
			NOKtoEURO();
			break;
		case 'c':
			mult_table();
			break;
		case 'd':
			solveQuadraticEquation();
			break;
		case 'e':
			calculateLoanPayments();
			break;
		case 'q':
			quit = true;
			break;
		default:
			cout << "::::::::::::::: UGYLDIG VALG :::::::::::::::" << endl;
		}
	}
	return 0;
}
