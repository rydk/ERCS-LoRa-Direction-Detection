clc
clear
for n=1:10
cd E:\data\left
data = loadBinData([num2str(n),'.dat']);
%data = loadBinData('1.dat');   
rawData=data(1:2:end)+data(2:2:end).*1i;
   
%% separate 2 antennas
unit = 16384;       
index = 1:1:length(rawData);
ind = rem(floor((index-1)/unit),2);
data1 = rawData(ind==0);
data2 = rawData(ind==1);

dataR1 = data1(abs(real(data2))>0.001&abs(imag(data2))>0.001);
dataR2 = data2(abs(real(data2))>0.001&abs(imag(data2))>0.001);

%% raw amp/phase of 2 antennas

dataS1 = dataR1;
dataS2 = dataR2;

amp_data1=abs(dataS1);
phase_data1=angle(dataS1);
pha_ur_data1=unwrap(phase_data1);

amp_data2=abs(dataS2);
phase_data2=angle(dataS2);
pha_ur_data2=unwrap(phase_data2);

%% signal ratio

dataRatio1 = dataS1./dataS2;
%dataRatio1 = dataS2./dataS1;

I = real(dataRatio1);
Q = imag(dataRatio1);

I = sgolayfilt(I,2,10^4-1);
Q = sgolayfilt(Q,2,10^4-1);

dataRatio = I + 1i*Q;

phase1=angle(dataRatio);
amp1=abs(dataRatio);
phase_ur1=unwrap(angle(dataRatio));


ratio_phase1 = sgolayfilt(phase1,2,10^3-1);
ratio_amp1=sgolayfilt(amp1,2,10^3-1);
ratio_phase_ur1= sgolayfilt(phase_ur1,2,10^3-1);

%% cfar
xc_amp=ratio_amp1(1:1000:end);
xc_phase=ratio_phase1(1:1000:end);
xc_phase_ur=ratio_phase_ur1(1:1000:end);

N=18;
pro_N=2;
PAD=10^(-4);
k=2.*N./4;
[index_amp, XT_amp] = cfar_ca(xc_amp, N, pro_N, PAD);
[index_phase, XT_phase] = cfar_ca(xc_phase, N, pro_N, PAD);
[index_phase_ur, XT_phase_ur] = cfar_ca(xc_phase_ur, N, pro_N, PAD);

 [XT_amp,PS1] = mapminmax(XT_amp,0,1);
 [XT_phase,PS2] = mapminmax(XT_phase,0,1);
 [XT_phase_ur,PS3] = mapminmax(XT_phase_ur,0,1);

figure;
subplot(2,1,1)
plot(XT_amp);
xlabel('Time (second)');
ylabel('Amplitude');
title('Ratio-amp');

subplot(2,1,2)
plot(xc_amp);hold on;
xlabel('Time (second)');
ylabel('Amplitude');
title('Ratio-amp');
end