clear all;close all;clc;

R = 40e-3;
r = linspace(0,R,1000);

v_max = 1;
k = [6 7 9];

v_lam = v_max * (1-r.^2./R^2);


v_turb = [];
for elem = k
    v_turb = [v_turb; v_max * (1 - r ./ R) .^ (1/elem)];
end;


plot(r,v_lam,r,v_turb(1,:),r,v_turb(2,:),r,v_turb(3,:));grid on;
legend('laminare Stroemung','turbulent: k = 6', 'turbulent: k = 7', 'turbulent: k=9');
