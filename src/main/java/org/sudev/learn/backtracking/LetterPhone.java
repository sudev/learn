package org.sudev.learn.backtracking;

import java.util.*;

import static java.util.Arrays.asList;

/**
 * @author sudev.ac on 23/05/20
 */
public class LetterPhone {
    static Map<Character, List<String>> mapper = new HashMap<>();

    static {
        mapper.put('1', Collections.singletonList("1"));
        mapper.put('0', Collections.singletonList("0"));
        mapper.put('2', asList("a", "b", "c"));
        mapper.put('3', asList("d", "e", "f"));
        mapper.put('4', asList("g", "h", "i"));
        mapper.put('5', asList("j", "k", "l"));
        mapper.put('6', asList("m", "n", "o"));
        mapper.put('7', asList("p", "q", "r", "s"));
        mapper.put('8', asList("t", "u", "v"));
        mapper.put('9', asList("w", "x", "y", "z"));
    }

    public static void main(String[] args) {
        ArrayList<String> result = letterCombinations("4023");
        System.out.println(result);
    }

    private static List<String> loop(String A, String accum) {
        if (A.isEmpty()) {
            List<String> result = new ArrayList<>();
            result.add(accum);
            return result;
        }
        Character headLetter = A.charAt(0);
        String tailString = A.substring(1);
        ArrayList<String> solution = new ArrayList<>();
        for (String elem : mapper.get(headLetter)) {
            solution.addAll(loop(tailString, accum + elem));
        }
        return solution;
    }

    public static ArrayList<String> letterCombinations(String A) {
        return (ArrayList<String>) loop(A, "");
    }
}
