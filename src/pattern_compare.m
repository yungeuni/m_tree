clc
clear all
close all

load stock.mat
load code.mat

Amplitude = zeros(length(code),1);
days = 300;

% figure;

for i = 1:length(code)
    if length(price{i}) > days
        S = price{code == 012450}(end-days:end,1);
        S = S/max(S);
        S = diff(S);
        
        T1 = price{i}(end-days:end,1);
        T1 = T1/max(T1);
        T1 = diff(T1);
        
        [C1,lag1] = xcorr(T1,S);
        Amplitude(i) = max(C1);

%         subplot(3,1,1);
%         plot(price{code == 012450}(end-days:end,1));
%         title(code_name{code_num == 012450});
% 
%         subplot(3,1,2);
%         plot(price{code(i)}(end-days:end,1));
% %         title(code_name{code_num == code(i)});
% 
%         subplot(3,1,3);
%         plot(lag1,C1,'k')
% %         title(code_name{code_num == code(i)});
%         
%         pause;


%         C1 = corrcoef(T1,S);
%         Amplitude(i) = C1(2);
    end

    
end

Amplitude = Amplitude/max(Amplitude);
[Y,idx] = sort(Amplitude);
best_stock = code(flipud(idx));

best_stock(1:5)

figure; hold on;

subplot(5,1,1);
plot(price{code == 012450}(end-days:end,1));

for i = 1:4
    subplot(5,1,i+1);
    plot(price{code == best_stock(i)}(end-days:end,1));
end







%  

% figure
% ax(1) = subplot(3,1,1); 
% plot(S);
% 
% ax(2) = subplot(3,1,2); 
% plot(T1);
% 
% ax(3) = subplot(3,1,3); 
% [C1,lag1] = xcorr(T1,S);
% plot(lag1,C1,'k')
% 

% s1 = alignsignals(T1,S);
% plot(s1,'k')




% figure
% ax(1) = subplot(2,1,1); 
% plot(lag1/Fs,C1,'k')
% ylabel('Amplitude')
% grid on
% title('Cross-correlation between Template 1 and Signal')
% ax(2) = subplot(2,1,2); 
% plot(lag2/Fs,C2,'r')
% ylabel('Amplitude') 
% grid on
% title('Cross-correlation between Template 2 and Signal')
% xlabel('Time(secs)') 
% axis(ax(1:2),[-1.5 1.5 -700 700 ])
% 



% 
% % plot(price{find(code == best_stock(1))}, 'r');
% % plot(price{find(code == best_stock(2))}, 'g');
% % plot(price{find(code == best_stock(2))}, 'b');
% % 
% % 
