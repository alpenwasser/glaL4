% FHNW Technik, Physiklabor, Experiment A11
% Lattice Plane Distances, other Crystals
% (c) Raphael Frey, April 2016

clear all;clc;

% Bergkristall (SiO)

bergkristall_Beta  = [25.2 50.0 80.4 119.6] .* pi ./ 180 .* 1/2;
bergkristall_Alpha = [27.6 55.6 87.2 132.4] .* pi ./ 180 .* 1/2;


% Kalkspat (CaCO3)

kalkspat_Beta  = [32.4 74.8] .* pi ./ 180 .* 1/2;
kalkspat_Alpha = [36.0 78.4] .* pi ./ 180 .* 1/2;


% Synthetischer Quartz (SiO)

synth_Quartz_Beta  = [40.4 90.0]  .* pi ./ 180 .* 1/2;
synth_Quartz_Alpha = [44.8 102.8] .* pi ./ 180 .* 1/2;

% Pyrit (FeS2)

pyrit_Beta  = [38.0] .* pi ./ 180 .* 1/2;
pyrit_Alpha = [42.0] .* pi ./ 180 .* 1/2;


% Fe-Anode
lambda_K_beta  = 175.66e-12;
lambda_K_alpha = (194.0 + 193.6) / 2 * 1e-12;

% Calculate lattice plane distance w/ Bragg equation

n = 1;
for angle = bergkristall_Beta
    bergkristall_d_Beta(n) = n * lambda_K_beta / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = bergkristall_Alpha
    bergkristall_d_Alpha(n) = n * lambda_K_alpha / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = kalkspat_Beta
    kalkspat_d_Beta(n) = n * lambda_K_beta / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = kalkspat_Alpha
    kalkspat_d_Alpha(n) = n * lambda_K_alpha / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = synth_Quartz_Beta
    synth_Quartz_d_Beta(n) = n * lambda_K_beta / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = synth_Quartz_Alpha
    synth_Quartz_d_Alpha(n) = n * lambda_K_alpha / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = pyrit_Beta
    pyrit_d_Beta(n) = n * lambda_K_beta / (2 * sin(angle));
    n = n+1;
end

n = 1;
for angle = pyrit_Alpha
    pyrit_d_Alpha(n) = n * lambda_K_alpha / (2 * sin(angle));
    n = n+1;
end


bergkristall_d_Beta_avg  =  mean(bergkristall_d_Beta)
bergkristall_d_Beta_err  =  std(bergkristall_d_Beta) * sqrt(1/length(bergkristall_d_Beta))
bergkristall_d_Alpha_avg =  mean(bergkristall_d_Alpha)
bergkristall_d_Alpha_err =  std(bergkristall_d_Alpha) * sqrt(1/length(bergkristall_d_Alpha))
bergkristall_d_avg       =  mean([bergkristall_d_Beta bergkristall_d_Alpha])
bergkristall_d_err       =  std([bergkristall_d_Alpha bergkristall_d_Beta]) * sqrt(1/length([bergkristall_d_Alpha bergkristall_d_Beta]))

kalkspat_d_Beta_avg  =  mean(kalkspat_d_Beta)
kalkspat_d_Beta_err  =  std(kalkspat_d_Beta) * sqrt(1/length(kalkspat_d_Beta))
kalkspat_d_Alpha_avg =  mean(kalkspat_d_Alpha)
kalkspat_d_Alpha_err =  std(kalkspat_d_Alpha) * sqrt(1/length(kalkspat_d_Alpha))
kalkspat_d_avg       =  mean([kalkspat_d_Beta kalkspat_d_Alpha])
kalkspat_d_err       =  std([kalkspat_d_Alpha kalkspat_d_Beta]) * sqrt(1/length([kalkspat_d_Alpha kalkspat_d_Beta]))

synth_Quartz_d_Beta_avg  =  mean(synth_Quartz_d_Beta)
synth_Quartz_d_Beta_err  =  std(synth_Quartz_d_Beta) * sqrt(1/length(synth_Quartz_d_Beta))
synth_Quartz_d_Alpha_avg =  mean(synth_Quartz_d_Alpha)
synth_Quartz_d_Alpha_err =  std(synth_Quartz_d_Alpha) * sqrt(1/length(synth_Quartz_d_Alpha))
synth_Quartz_d_avg       =  mean([synth_Quartz_d_Beta synth_Quartz_d_Alpha])
synth_Quartz_d_err       =  std([synth_Quartz_d_Alpha synth_Quartz_d_Beta]) * sqrt(1/length([synth_Quartz_d_Alpha synth_Quartz_d_Beta]))

pyrit_d_Beta_avg  =  mean(pyrit_d_Beta)
pyrit_d_Beta_err  =  std(pyrit_d_Beta) * sqrt(1/length(pyrit_d_Beta))
pyrit_d_Alpha_avg =  mean(pyrit_d_Alpha)
pyrit_d_Alpha_err =  std(pyrit_d_Alpha) * sqrt(1/length(pyrit_d_Alpha))
pyrit_d_avg       =  mean([pyrit_d_Beta pyrit_d_Alpha])
pyrit_d_err       =  std([pyrit_d_Alpha pyrit_d_Beta]) * sqrt(1/length([pyrit_d_Alpha pyrit_d_Beta]))