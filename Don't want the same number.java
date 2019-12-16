import java.util.*;

public class Solution {
	public int[] solution(int []arr) {
        ArrayList <Integer> list = new ArrayList<Integer>();
        int nowNum = 10;
        for(int a=0; a<arr.length; a++){
            if(arr[a] != nowNum){
                list.add(arr[a]);
                nowNum = arr[a];
            }
        }
        int[] answer = new int[list.size()];
        for(int b=0; b<list.size(); b++){
            answer[b] = list.get(b);
        }

        return answer;
				//fsefd
				
	}
}
