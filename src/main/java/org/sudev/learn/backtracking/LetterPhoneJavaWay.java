package org.sudev.learn.backtracking;

import java.util.ArrayList;

/**
 * @author sudev.ac on 23/05/20
 */
// Interview bits standard solution
public class LetterPhoneJavaWay {
    static String[] map = new String[]{"0", "1", "abc", "def", "ghi", "jkl", "mno",
            "pqrs", "tuv", "wxyz"};

    public static void main(String[] args) {
        ArrayList<String> strings = letterCombinations("0123");
        System.out.println(strings);
    }

    public static ArrayList<String> letterCombinations(String A) {
        ArrayList<String> ans = new ArrayList<String>();
        back(A, ans, "", 0);
        return ans;
    }

    public static void back(String A, ArrayList<String> ans, String str, int index) {
        if (index >= A.length()) {
            ans.add(str);
            return;
        }
        int idx = (int) (A.charAt(index) - '0');
        String temp = map[idx];
        for (int j = 0; j < temp.length(); j++) {
            back(A, ans, str + temp.charAt(j), index + 1);
        }
    }
}
