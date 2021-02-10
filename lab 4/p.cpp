#include<bits/stdc++.h>
using namespace std;
#define ll long long
bool f(string s){
    for(auto i:s){
        if(i<'0'||i>'9')
            return 0;
    }
    return 1;
}
void inv_case(){
    cout<<"INVALID\n";
    freopen("output.txt","w",stdout);
    cout<<"INVALID\n";
}

ll com(int n,int r){
    //if(n==)
    //cout<<"n: "<<n<<" r:"<<r<<"   =>";
    ll num=1,den=1;
    for(int i=1;i<=r;i++){
        num*=n;
        n--;
        den*=i;
    }
    //cout<<"num: "<<num<<" den: "<<den;
    return num/den;
}
ll cal(int n,int x,int y,int z,int i,int j){
    int ans=(com(x,n-i-j)*com(y,i)*com(z,j));
    return ans;
}
int main(){
    string a,b,c,d;
    cout<<"enter N,X,Y,Z: ";
    cin>>a>>b>>c>>d;
    bool invalid=0;
    if(!f(a) || !f(b) || !f(c) || !f(d))invalid=1;

    if(invalid){
        inv_case();
        return 0;
    }

    ll n,x,y,z;
    n=stoi(a);
    x=stoi(b);
    y=stoi(c);
    z=stoi(d);

    if(n>x+y+z){
        inv_case();
        return 0;
    }
    cout<<"X: "<<x<<"  Y: "<<y<<"  Z: "<<z<<'\n';
    ll tot=com(x+y+z,n);
    vector<int>g(n+1,0),h(n+1,0);
    cout<<"Intermediate results:\n\n";
    cout<<"total number of ways of selecting "<<n<<" pens = "<<tot<<'\n';
    cout<<"below are possible value of f(y,z) for y going from 0 to "<<n<<" and z going from 0 to "<<n<<" and 0<=y+z<="<<n<<"\n\n";
    // for(int sum=0;sum<=n;sum++){
    //  for(int i=0;i<=sum;i++){
    //      int j=sum-i;
    //      ll num=cal(n,x,y,z,i,j);
    //      g[j]+=num;
    //      h[i]+=num;
    //      cout<<"f("<<i<<","<<j<<")= "<<num<<"/"<<tot<<"= "<<1.0*num/tot<<'\n';
    //  }
    // }
    for(int i=0;i<=n;i++){
        for(int j=0;j<=n;j++){

            ll num=0;
            if(i+j<=n)
                num=cal(n,x,y,z,i,j);
            g[j]+=num;
            h[i]+=num;
            cout<<"f("<<i<<","<<j<<")= "<<num<<"/"<<tot<<"= "<<1.0*num/tot<<'\n';
        }
    }
    
    cout<<"\n---------Marginal probabilities---------\n";
    cout<<"for y :\n";
    for(int i=0;i<=n;i++){
        cout<<"h("<<i<<")="<<h[i]<<"/"<<tot<<'\n';
    }
    cout<<"\nfor z :\n";
    for(int i=0;i<=n;i++){
        cout<<"g("<<i<<")="<<g[i]<<"/"<<tot<<'\n';
    }
    cout<<"\nJoint probability function: f(y,z)=(C("<<x<<","<<n<<"-y-z)*C("<<y<<",y)*C("<<z<<",z)/C("<<x+y+z<<","<<n<<"))\n";

    freopen("output.txt","w",stdout);

    cout<<"X: "<<x<<"  Y: "<<y<<"  Z: "<<z<<'\n';
    cout<<"Intermediate results:\n\n";
    cout<<"total number of ways of selecting "<<n<<" pens = "<<tot<<'\n';
    cout<<"below are possible value of f(y,z) for y going from 0 to "<<n<<" and z going from 0 to "<<n<<" and 0<=y+z<="<<n<<"\n\n";
    for(int i=0;i<=n;i++){
        for(int j=0;j<=n;j++){

            ll num=0;
            if(i+j<=n)
                num=cal(n,x,y,z,i,j);
            cout<<"f("<<i<<","<<j<<")= "<<num<<"/"<<tot<<"= "<<1.0*num/tot<<'\n';
        }
    }
    cout<<"\n---------Marginal probabilities---------\n";
    cout<<"for y :\n";
    for(int i=0;i<=n;i++){
        cout<<"h("<<i<<")="<<h[i]<<"/"<<tot<<'\n';
    }
    cout<<"\nfor z :\n";
    for(int i=0;i<=n;i++){
        cout<<"g("<<i<<")="<<g[i]<<"/"<<tot<<'\n';
    }
    cout<<"\nJoint probability function: f(y,z)=(C("<<x<<","<<n<<"-y-z)*C("<<y<<",y)*C("<<z<<",z)/C("<<x+y+z<<","<<n<<"))\n";

}