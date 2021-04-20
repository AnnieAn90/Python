tic

H = [4 1; 1 2];
f = [1 1]';

Aeq = [1,1];
beq = 1;

A = [2 0; 0 0.3];
b = [0.7,0.7]';

[x,fval] = quadprog(H,f,A,b,Aeq,beq)
toc