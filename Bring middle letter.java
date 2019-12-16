class Solution {
  public String solution(String s) {
      int a = s.length();
      String answer = "";

      if(a%2 == 1) {
          int b = a/2;
          answer = s.substring(b,b+1);
      } else {
          int b = a/2-1;
          answer = s.substring(b,b+2);
      }
      return answer;
    }
    public static void  main(String[] args){
        Solution s = new Solution();
        System.out.println(s.solution("power"));
        System.out.println(s.solution("test1234"));
        #sdfefsd
    }
}
