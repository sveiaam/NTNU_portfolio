using PyPlot
using QuadGK

matplotlib[:rc]("text", usetex=false) # allow tex rendering
#rc("font", family="sans-serif", weight="normal", size="18")
#rc("axes", labelsize="18")

function Cᵥ_DulongPetit(T, ϑ)
	return 1
end

function Cᵥ_Einstein(T, ϑ)
	return (ϑ/T)^2 * (exp(ϑ/T))/(exp(ϑ/T)-1)^2
end

function Cᵥ_Debye(T, ϑ)
	xD = ϑ/T
	intDebye(x) = x^4*exp(x)/(exp(x)-1)^2

	return 3*(T/ϑ)^3*quadgk(intDebye, 0, xD)[1]
end

function Cᵥ_Debye_lowtemp(T, ϑ)
	return 4*pi^4/5 * (T/ϑ)^3
end

function main()
	T = (ϴ_Pb = 105, ϴ_Si = 645)
	names = ("lead (Pb)", L"silicon (Si)")

	#Values of x in the range between 1 and 1000K
	x = collect(1:1:700)

	for ϑ in 1:length(T)
		y_DulongPetit = zeros(length(x))
		y_Einstein = zeros(length(x))
		y_Debye = zeros(length(x))
		y_Debye_lowtemp = zeros(length(x))
		for i in 1:length(x)
			y_DulongPetit[i] = Cᵥ_DulongPetit(x[i], T[ϑ])
			y_Einstein[i] = Cᵥ_Einstein(x[i], T[ϑ])
			y_Debye[i] = Cᵥ_Debye(x[i], T[ϑ])
			y_Debye_lowtemp[i] = Cᵥ_Debye_lowtemp(x[i], T[ϑ])
		end

		#Plot
		plot(x, y_DulongPetit, label="Dulong-Petit model")
		plot(x, y_Einstein, label="Einstein model")
		plot(x, y_Debye, label="Debye model")
		plot(x, y_Debye_lowtemp, label="Debye low temp. approx")

		xlabel(L"T")
		ylabel(L"C_{v}/3NK_{B}")
		ylim(0, 1.5)
		#title("Heat capacity for %s ." %names[ϑ])
		grid()
		legend()
		show()
		gcf()
		#clf()
	end
end

main()
