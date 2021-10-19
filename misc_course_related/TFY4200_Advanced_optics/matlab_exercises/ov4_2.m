%ov4_2.m
%Svein Åmdal

syms ck w w_t e_s e_inf
eqn = ck^2 / ( e_inf + (e_s - e_inf) / (1-w^2/w_t^2) ) - w^2 == 0;
sol = solve(eqn, w);
disp(sol);

%Substitute in some of the parameters and plot with respect to the
%remaining one
sol2 = subs(sol, [e_s, e_inf, w_t], [12.685, 10.6, 268]);
fplot(sol2, [0 1000]);
ylabel('\omega [cm^{-1}]')
xlabel('ck')

%%% NB: Usually, one is content with only the omega > 0 - section of this
%%% plot, giving a more well-known dispersion graph.