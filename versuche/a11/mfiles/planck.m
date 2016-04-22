% FHNW Technik, Physiklabor, Experiment A11, Wavelengths for regression
% for determining Planck constant.
% (c) Raphael Frey, April 2016

clear all;clc
format long;

% Errors, manually read from plots
angles_raw = [ 9   9.8 11.5 14.2 16.9 20.1 24.5 28.9];
errors_raw = [ 1.5 0.5  2.5  0.5  0.1  0.1  0.7  0.5];

% Offset and its error margin
npf_abs = -7.1352e-1 / 180 * pi;
npf_err = 3.627e-2 / 180 * pi;

% Convert from counting tube angle to Bragg angle, convert from degrees to radians
angles = angles_raw ./ 180 .* pi .* 1/2;
errors = errors_raw ./ 180 .* pi .* 1/2;

% Lattice plane distance in meters
d = 201.5e-12;

% order
n = 1;


% Offset angle correction, base value
offset_fixed_angles = angles - npf_abs;

i = 1;
for element = angles_raw
    % Error propagation for error for offset angle
    offset_fixed_error = sqrt(npf_err^2 + (errors(i))^2);
    
    % Calculate wavelengths: base values and error margins
    lambda(i) = 2*d*sin(offset_fixed_angles(i))/n;
    lambda_err(i) = 2*d*sin(offset_fixed_error)/n;
    
    i = i+1;
end

% Results
lambda
lambda_err
