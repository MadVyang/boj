#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int board[505][505];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n,m,b;
  cin>>n>>m>>b;
  for (int i=0;i<n;i++){
      for (int j=0;j<m;j++){
          cin>>board[i][j];
      }
  }

  int ans = 1234567890;
  int ans_h= 0;
  int cost=0;
  int mx=0;
  
  for (int i=0;i<n;i++){
      for (int j=0;j<m;j++){
          mx = max(mx, board[i][j]);
      }
  }
  while(mx>=0){
      int re=0;
      for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            re += mx - board[i][j];
        }
     }
     if (re<=b && ans>cost+re) {
         ans=cost+re;
         ans_h=mx;
     }
     
      for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (board[i][j]==mx) {
                board[i][j]--;
                cost+=2;
                b++;
            }
        }
     }
     mx--;
  }

cout<<ans<<" "<< ans_h<<endl;


  return 0;
}