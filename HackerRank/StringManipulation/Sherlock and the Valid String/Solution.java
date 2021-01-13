import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the isValid function below.
    static String isValid(String s) {
        
        int str_len = s.length();
        int letter_ocurrences[] = new int[26];
        for(int i = 0; i < 26; i++) letter_ocurrences[i] = 0;
        
        for(int i = 0; i < str_len; i++)
            letter_ocurrences[s.charAt(i)-97] += 1;
        
        for(int i = 0; i < 26; i++) System.out.print(letter_ocurrences[i]+" ");

        HashMap<Integer, Integer> ocu_ocu = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < 26; i++){
            int j = letter_ocurrences[i];
            if(j != 0){
                if(ocu_ocu.containsKey(j))
                    ocu_ocu.put(j, ocu_ocu.get(j) + 1);
                else
                    ocu_ocu.put(j, 1);
            }
        }

        System.out.println("\n"+ocu_ocu.toString());
        
        if(ocu_ocu.size() > 2) return "NO";
        if(ocu_ocu.size() == 1) return "YES";
        

        
   	    int f[] = new int[2];
        int i = 0;
        for (Integer integer : ocu_ocu.keySet()) {
        	f[i++] = integer;
		}

		i = Math.max(f[0], f[1]);
		int min = Math.min(f[0], f[1]);

		if(ocu_ocu.get(f[0]) == 1 || ocu_ocu.get(f[1]) == 1)
			if((ocu_ocu.get(i) == 1 && Math.abs(f[0]-f[1]) == 1) || (min == 1 && ocu_ocu.get(min) == 1))
				return "YES";
        

        return "NO";
    
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        

         String s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd";
    	//String s = "aaaabc";
        String result = isValid(s);
        System.out.println(result);

    }
}
