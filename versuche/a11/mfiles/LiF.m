% FHNW Technik, Physiklabor, Experiment A11
% Lattice Plane Distances, LiF
% (c) Raphael Frey, April 2016

clear all;clc

% offset angles (including conversion)
offset_Cu     = -7.2925e-1 * pi / 180 * 1/2;
offset_Cu_err = 8.0931e-2  * pi / 180 * 1/2;
offset_Fe     = -7.0575e-1 * pi / 180 * 1/2;
offset_Fe_err = 2.3094e-2  * pi / 180 * 1/2;
offset_Mo     = -7.0555e-1 * pi / 180 * 1/2;
offset_Mo_err = 6.8961e-2  * pi / 180 * 1/2;


% Peak angles (including conversions)
peaks_Cu_beta  = [39.2 85.6]      .* pi ./ 180 .* 1/2;
peaks_Cu_alpha = [43.6 98.0]      .* pi ./ 180 .* 1/2;
peaks_Fe_beta  = [50.4 120.0]     .* pi ./ 180 .* 1/2;
peaks_Fe_alpha = [56.0 146.8]     .* pi ./ 180 .* 1/2;
peaks_Mo_beta  = [16.7 34.8]      .* pi ./ 180 .* 1/2;
peaks_Mo_alpha = [19.2 40.0 62.0] .* pi ./ 180 .* 1/2;


% lambda_K
lambda_K_beta_Cu  = 139.23e-12;
lambda_K_alpha_Cu = (154.44 + 154.05)/2*1e-12;
lambda_K_beta_Fe  = 175.66e-12;
lambda_K_alpha_Fe = (194.0 + 193.6)/2*1e-12;
lambda_K_beta_Mo  = 63.26e-12;
lambda_K_alpha_Mo = (71.36+70.93)/2*1e-12;

% Lattice distances and errors (via Gauss error propagation), in meters
results = [
    1 * lambda_K_beta_Cu/(2*sin(peaks_Cu_beta(1) - offset_Cu)),
    2 * lambda_K_beta_Cu/(2*sin(peaks_Cu_beta(2) - offset_Cu)),
    1 * lambda_K_alpha_Cu/(2*sin(peaks_Cu_alpha(1) -offset_Cu)),
    2 * lambda_K_alpha_Cu/(2*sin(peaks_Cu_alpha(2) -offset_Cu)),
    1 * lambda_K_beta_Fe/(2*sin(peaks_Fe_beta(1) - offset_Fe)),
    2 * lambda_K_beta_Fe/(2*sin(peaks_Fe_beta(2) - offset_Fe)),
    1 * lambda_K_alpha_Fe/(2*sin(peaks_Fe_alpha(1) - offset_Fe)),
    2 * lambda_K_alpha_Fe/(2*sin(peaks_Fe_alpha(2) - offset_Fe)),
    1 * lambda_K_beta_Mo/(2*sin(peaks_Mo_beta(1) - offset_Mo)),
    2 * lambda_K_beta_Mo/(2*sin(peaks_Mo_beta(2) - offset_Mo)),
    1 * lambda_K_alpha_Mo/(2*sin(peaks_Mo_alpha(1) - offset_Mo)),
    2 * lambda_K_alpha_Mo/(2*sin(peaks_Mo_alpha(2) - offset_Mo)),
    3 * lambda_K_alpha_Mo/(2*sin(peaks_Mo_alpha(3) - offset_Mo))
]

mean(results)
std(results) * sqrt(1/length(results))
