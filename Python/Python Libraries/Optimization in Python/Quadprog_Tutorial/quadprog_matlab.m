%% Case 1
% 
% H = [4 1; 1 2];
% f = [1 1]';
% 
% Aeq = [1,1];
% beq = 1;
% 
% A = [2 0; 0 0.3];
% b = [0.7,0.7]';
% 
% tic
% [x,fval] = quadprog(H,f,A,b,Aeq,beq)
% toc

%% case 2
clear all
M = [1 2 0; -8 3 2; 0 1 1];
b_bar = [3 2 3]';
H = M'*M;
f = -M'*b_bar;

A = [1 2 1; 2 0 1; -1 2 -1];
b = [3;2;-2];

tic
[x,fval] = quadprog(H,f,A,b)
toc