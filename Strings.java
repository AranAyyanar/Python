import java.util.*;
class Strings{
  public static void main(String[] args){
  Scanner scan= new Scanner(System.in);
  String[] list1=new String[2];
  int[] list4=new int[2];
  for(int i=0;i<2;i++){
     list1[i]=scan.nextLine();
  }
  String[] list2=list1[0].split(" ");
  String[] list3=list1[1].split("");
  for(int i=0;i<2;i++){
     int N=Integer.parseInt(list3[i]);
     list4[i]=N;
  }
  String[] listr=new String[list2.length];
  for (int i=0;i<list2.length;i++){
      String rev="";
      int k=list2[i].length()/2;
      if (k>=2){
         for(int j=k-1;j>=0;j--){
            rev=rev+list2[i].charAt(j);
         }
         for(int j=k;j<(list2[i].length());j++){
            rev=rev+list2[i].charAt(j);
         }
         listr[i]=rev;
      }
      else{
         listr[i]=list2[i];
      }
  }
  System.out.println(listr[list4[0]+1]+" "+listr[list4[1]+1]);
  }
}
