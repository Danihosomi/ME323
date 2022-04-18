#include <bits/stdc++.h>
int n, p;
std::vector<int> v;

void ans(int id,int sum){ // Recursão que calcula em quantos casos, temos que X será igual a sum. 
    if(!id){
        v[sum]++;
        return ;
    }
    for(int i=1;i<=n;i++) ans(id-1,sum+i);
}

int main(){
    std::cin>>n>>p; v.resize(p*n+5);
    ans(p,0);

    for(int i=0;i<=18;i++) std::cout<<"Probabilidade de X="<<i<<" eh "<<(double)((double)(v[i])/(double)(125))<<'\n';

    return 0;
}